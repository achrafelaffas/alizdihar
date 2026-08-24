# -*- coding: utf-8 -*-
from odoo import api, fields, models


class DailyExpenseReport(models.Model):
    _name = 'daily.expense.report'
    _description = 'Daily Expense Report'
    _order = 'date desc, id desc'

    name = fields.Char(
        string='Reference',
        compute='_compute_name',
        store=True,
    )
    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.context_today,
    )
    product_id = fields.Many2one(
        'product.product',
        string='Product',
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
    )
    entry = fields.Float(string='Entry')
    purchase = fields.Float(string='Purchase')
    wage = fields.Float(string='Wage')
    other_expenses = fields.Float(string='Other Expenses')
    lhaj_expenses = fields.Float(string='Lhaj Expenses')
    rest = fields.Float(
        string='Rest',
        compute='_compute_rest',
        store=True,
        help='Entry - (Purchase + Wage + Other Expenses + Lhaj Expenses)',
    )
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
    )

    @api.depends('entry', 'purchase', 'wage', 'other_expenses', 'lhaj_expenses')
    def _compute_rest(self):
        for record in self:
            record.rest = record.entry - (
                record.purchase
                + record.wage
                + record.other_expenses
                + record.lhaj_expenses
            )

    @api.depends('date', 'product_id', 'employee_id')
    def _compute_name(self):
        for record in self:
            parts = []
            if record.date:
                parts.append(fields.Date.to_string(record.date))
            if record.product_id:
                parts.append(record.product_id.display_name)
            if record.employee_id:
                parts.append(record.employee_id.display_name)
            record.name = ' - '.join(parts) if parts else 'New'
