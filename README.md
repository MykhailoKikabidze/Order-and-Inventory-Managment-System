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

Planning and initial setup.

The `backend/` directory contains the uv project configuration. It uses Python
3.11.2, as specified in `.python-version` at the repository root. Django and
other dependencies will be added in a later step.
