FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

WORKDIR /usr/src/app

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .
