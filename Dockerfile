FROM python:3.12-slim

RUN useradd sandboxuser

COPY requirements-freeze.txt .
RUN pip install --no-cache-dir -r requirements-freeze.txt

COPY src /app
WORKDIR /app

USER sandboxuser

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]