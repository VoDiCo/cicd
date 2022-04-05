FROM python:3.8-alpine3.14

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD ./cicd .

RUN pip install -r requirements.txt
