FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py /app/
COPY .env /app/

CMD ["python3", "create_tables.py"]
CMD ["python3", "forecasts.py"]