FROM python:3.7-alpine
MAINTAINER Renan Moura

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
RUN chown -R user:user /app
RUN chmod 755 /app
USER user
