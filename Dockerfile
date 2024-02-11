FROM python:3.8-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.locked.txt /requirements.locked.txt
RUN pip install --prefix=/install -r /requirements.locked.txt
FROM base
COPY --from=builder /install /usr/local
COPY src /app
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
