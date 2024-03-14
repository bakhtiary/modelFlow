FROM python:3.10-alpine as base
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.locked.txt /requirements.locked.txt
RUN pip install --prefix=/install -r /requirements.locked.txt
FROM base
COPY --from=builder /install /usr/local
COPY src /app
WORKDIR /app
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
