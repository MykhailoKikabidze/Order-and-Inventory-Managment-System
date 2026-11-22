# Order and Inventory Management System

An internal system for managing products, warehouse stock, and customer orders—from reserving items to preparing and shipping orders.

## Project goals

- Keep stock information accurate across warehouses.
- Prevent the same products from being reserved for multiple orders.
- Help employees track and process orders.
- Provide a practical backend project built in manageable stages.

## MVP scope

The first version will allow employees to:

- Manage products, warehouses, and stock.
- Create draft orders and confirm them when stock is available.
- Reserve stock and release it when an unshipped order is cancelled.
- Track orders through preparation and shipment.
- Access features according to their role.

Payments, returns, external integrations, and advanced reporting are outside the initial scope.

## Planned technology

- Python and Django
- Django REST Framework
- PostgreSQL
- Docker
- GitHub Actions

Redis and other technologies may be added later when needed.

## Project status

Initial Django project setup is complete. Products, orders, and inventory
features are not implemented yet.

## Local setup

### Prerequisites

- Python 3.11.2, as specified in `.python-version`
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- PostgreSQL 14 or newer, with a running server, a database, and a user
  permitted to create tables in that database

From the repository root, install the dependencies and create a local
configuration file:

```bash
cd backend
uv sync
cp .env.example .env
```

Edit `backend/.env` with your PostgreSQL database name, user, password, host,
and port. The `.env` file is ignored by Git; do not commit it or share its
contents. The `.env.example` file documents the required variables without
containing real credentials.

Apply migrations to create Django's tables in PostgreSQL:

```bash
uv run python manage.py migrate
```

Start the development server from `backend/`:

```bash
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser. Press Ctrl+C in the terminal to
stop the server. The development server and default settings are not intended
for production.
