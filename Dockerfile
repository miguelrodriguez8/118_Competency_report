FROM python:3.8-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    musl-dev \
    openssl \
    postgresql \
    libpq-dev

COPY requirements/requirements.txt ./requirements/requirements.txt
RUN pip install -r ./requirements/requirements.txt

COPY manage.py ./manage.py
COPY setup.cfg ./setup.cfg
COPY mtbfinder_website ./mtbfinder_website

EXPOSE 8000

FROM production as development

COPY requirements/dev.txt ./requirements/dev.txt
RUN pip install -r ./requirements/dev.txt

COPY . .
