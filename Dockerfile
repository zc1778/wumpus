FROM alpine

WORKDIR /app

COPY . .

RUN apk add python3