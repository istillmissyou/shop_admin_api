FROM tiangolo/uvicorn-gunicorn:python3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y netcat

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .
