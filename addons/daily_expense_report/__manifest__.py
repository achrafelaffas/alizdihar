# -*- coding: utf-8 -*-
{
    'name': 'Daily Expense Report',
    'version': '19.0.1.0.0',
    'category': 'Accounting',
    'summary': 'Daily tracking of entries, purchases, wages and expenses per product/employee',
    'description': """
Daily Expense Report
=====================
Track, per day, the following amounts linked to a product and an employee:

* Entry
* Purchase
* Wage
* Other Expenses
* Lhaj Expenses
* Rest (computed automatically = Entry - (Purchase + Wage + Other Expenses + Lhaj Expenses))

Features:
* Inline editable list view (edit directly in the list, no need to open the form)
* Group by Day / Week / Month / Quarter / Year on the Date field
* Grouped by Day by default
* Dedicated root menu
* French translation included
""",
    'author': 'Karizma Consulting Group',
    'license': 'LGPL-3',
    'depends': ['base', 'product', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/daily_expense_views.xml',
        'views/daily_expense_menu.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
