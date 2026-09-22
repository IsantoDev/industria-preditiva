FROM python:3.12-slim

WORKDIR /app

COPY requirements-api.txt .
RUN pip install --no-cache-dir -r requirements-api.txt

COPY . .
RUN pip install --no-chahce-dir -e .

EXPOSE 7860
CMD ["uvicorn", "industria.api:app", "--host", "0.0.0.0", "--port", "7860"]