FROM python:3.6.1-slim

RUN apt-get update && \
    apt-get install -y libpq-dev gcc wget unzip vim htop

COPY "$PWD/" /app/

WORKDIR /app
RUN pip install -r requirements.txt

