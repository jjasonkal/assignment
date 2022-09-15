FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY *.py /app/
COPY .env /app/
COPY docker_entrypoint.sh /app/
COPY /csv csv

RUN chmod a+x docker_entrypoint.sh

CMD ["./docker_entrypoint.sh"]