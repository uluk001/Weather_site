FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY ./requirements.txt .
RUN pip install -r requirements.txt
# Установка supervisord

COPY . .
COPY ../.env ./.env
EXPOSE 8000

RUN chmod +x ./entrypoint.sh

ENTRYPOINT [ "bash", "-c", "./entrypoint.sh"]
