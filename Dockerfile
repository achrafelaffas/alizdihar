FROM odoo:19

USER root

# Copy custom and enterprise addons into the image
COPY ./addons /mnt/extra-addons
COPY ./enterprise /mnt/extra-addons/enterprise

# Copy your Odoo config
COPY ./odoo.conf /etc/odoo/odoo.conf

# Make sure the odoo user can read everything
RUN chown -R odoo:odoo /mnt/extra-addons /etc/odoo/odoo.conf

USER odoo

EXPOSE 8069