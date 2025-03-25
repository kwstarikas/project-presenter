FROM python:3.13  

RUN mkdir -p /app  

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

WORKDIR /app
COPY requirements.txt  /app/
RUN pip install -r requirements.txt --no-cache-dir

COPY . /app/
