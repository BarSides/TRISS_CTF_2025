FROM python:3.13-slim@sha256:0222b795db95bf7412cede36ab46a266cfb31f632e64051aac9806dabf840a61

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY templates/ templates/
COPY static/ static/
COPY flag.txt .

COPY app.py .
COPY rules.py .

EXPOSE 5000

CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "app:app"]
