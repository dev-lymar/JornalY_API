FROM python:3.12.2-slim

WORKDIR app/

COPY requirements.txt /app

RUN pip install --upgrade pip \
 && pip install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "jornaly_api.wsgi:application", "--bind", "0:8000"]