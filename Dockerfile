FROM debian:10
RUN apt-get update && apt-get install -y build-essential rebar vim-tiny

ADD . /app/
WORKDIR /app
