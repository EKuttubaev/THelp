FROM python:3.9.0-alpine

WORKDIR /code

COPY requirements.txt .

COPY src/ .

RUN apk add musl-dev postgresql-libs postgresql-dev gcc linux-headers

RUN pip install -r requirements.txt

CMD ["uwsgi", "--http", ":8000", "--module", "customs.wsgi"]