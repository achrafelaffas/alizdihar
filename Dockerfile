services:
  db:
    image: postgres:16
    container_name: odoo19-db
    restart: unless-stopped
    environment:
      POSTGRES_DB: postgres
      POSTGRES_USER: odoo
      POSTGRES_PASSWORD: odoo
    volumes:
      - postgres_data:/var/lib/postgresql/data

  odoo:
    image: odoo:19
    container_name: odoo19
    restart: unless-stopped
    depends_on:
      - db
    ports:
      - "8080:8069"
    environment:
      HOST: db
      USER: odoo
      PASSWORD: odoo
    volumes:
      - odoo_data:/var/lib/odoo
      # Optional: custom addons
      - ./addons:/mnt/extra-addons
      - ./enterprise:/mnt/extra-addons/enterprise
      # Optional: custom config
      - ./odoo.conf:/etc/odoo/odoo.conf

volumes:
  postgres_data:
  odoo_data: