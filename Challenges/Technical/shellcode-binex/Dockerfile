FROM ubuntu:latest

EXPOSE 9999

RUN apt-get update && apt-get install -y socat \
	&& apt-get install -y clang \
	&& apt-get install -y gcc \
	&& apt-get install -y make

WORKDIR /app

COPY ./pub/challenge.c ./pub/Makefile ./priv/flag.txt ./
RUN cd /app && make


CMD socat TCP4-LISTEN:9999,fork EXEC:/app/british-oil-company

