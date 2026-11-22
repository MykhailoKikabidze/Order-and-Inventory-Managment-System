FROM python:3.11.2-slim

WORKDIR /app

RUN pip install uv==0.12.4

COPY pyproject.toml .
COPY uv.lock .
RUN uv sync --frozen --no-dev

COPY . .

CMD [".venv/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]