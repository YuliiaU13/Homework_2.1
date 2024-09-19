FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install psycopg2
RUN pip install -r requirements.txt

CMD ["pytest", "test_db_docker_file.py"]
