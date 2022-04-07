FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD ./cicd /app

RUN pip install -r requirements.txt
