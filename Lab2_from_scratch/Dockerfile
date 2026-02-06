FROM golang:1.22-alpine AS builder

WORKDIR /app
COPY main.go .

RUN GO111MODULE=off go build -o hello2 main.go


FROM alpine:latest

WORKDIR /app
COPY --from=builder /app/hello2 .

CMD ["./hello2"]