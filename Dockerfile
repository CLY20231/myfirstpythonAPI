FROM python:3.9.7-slim

WORKDIR /api
COPY . /api

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --skip-lock --dev

CMD ["pipenv", "run", "main"]