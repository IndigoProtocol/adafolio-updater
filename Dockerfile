FROM python:alpine

COPY . /app
WORKDIR /app
RUN pip install .
