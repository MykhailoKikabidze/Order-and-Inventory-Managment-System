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
- Docker with Docker Compose, with the Docker engine running

From the repository root, create a local configuration file if you don't
already have one:

```bash
cp backend/.env.example backend/.env
```

Edit `backend/.env` with a database name, user, and password for local
development. Set `POSTGRES_HOST=127.0.0.1` and `POSTGRES_PORT=5433` so Django
running on your computer connects to the Compose database. The `.env` file is
ignored by Git; do not commit it or share its contents. The `.env.example`
file documents the required variables without containing real credentials.

Build and start Django and PostgreSQL from the repository root:

```bash
docker compose --env-file backend/.env up -d --build
docker compose --env-file backend/.env ps
```

Compose waits for PostgreSQL to be healthy before starting Django. Docker
stores database data in a named volume, so it persists when the container is
recreated. PostgreSQL uses the database, user, and password in `.env` only
when initializing an empty volume; changing those values later does not
update an existing database.

Apply migrations separately to create Django's tables; they do not run
automatically when the app starts:

```bash
docker compose --env-file backend/.env exec app .venv/bin/python manage.py migrate
```

Open http://127.0.0.1:8000/ in your browser. After changing application code,
rebuild the image with `docker compose --env-file backend/.env up -d --build`.
To stop the services without removing their data:

```bash
docker compose --env-file backend/.env stop
```

The development server and default settings are not intended for production.

### Running tests

With the Compose database running, install the development dependencies and
run the tests from `backend/`:

```bash
cd backend
uv sync
uv run pytest
```

The PostgreSQL user needs permission to create databases. Django creates and
removes a separate test database; it does not run tests against the configured
development database. The application image does not include test dependencies.

### Running Django outside Docker

Alternatively, start only PostgreSQL with
`docker compose --env-file backend/.env up -d db`, then run Django locally:

```bash
cd backend
uv sync
uv run python manage.py migrate
uv run python manage.py runserver
```

Press Ctrl+C to stop the local development server.
