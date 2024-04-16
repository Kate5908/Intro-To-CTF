FROM ubuntu:latest

EXPOSE 9999

RUN apt-get update && apt-get install -y socat \
	&& apt-get install -y clang \
	&& apt-get install -y gcc \
	&& apt-get install -y make

WORKDIR /app

COPY ./source.c
RUN cd /app && gcc source.c -o source --no-pie -O0 -fno-stack-protector


CMD socat TCP4-LISTEN:9999,fork EXEC:/app/source