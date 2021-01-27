FROM debian:10
#FROM alpine:3

#ENV PYTHONBUFFERED=1

WORKDIR /root/

#RUN apk add --no-cache python3 && \
#      python3 -m ensurepip && \
#      pip3 install --no-cache --upgrade pip setuptools wheel
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
      python3 \
      python3-pip
RUN pip3 install pip --upgrade

RUN pip3 install \
      watchdog \
      click \
      nrfutil

COPY coap-dfu-server.py coap-dfu-server.py
COPY dfu_entrypoint.sh  dfu_entrypoint.sh

ENTRYPOINT ["./dfu_entrypoint.sh"]

