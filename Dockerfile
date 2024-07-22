FROM python:3.12.2-slim

WORKDIR app/

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "jornaly_api.wsgi:application", "--bind", "0:8000"]