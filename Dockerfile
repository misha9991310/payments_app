FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /paymentsapp
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .
EXPOSE 8000