FROM python:3.12-slim

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .
RUN pip install --no-cache-dir -e .

# Usuário não-root (hardening de segurança)
RUN useradd -m appuser && chown -R appuser /app
USER appuser

CMD uvicorn industria.api:app --host 0.0.0.0 --port ${PORT:-7860}