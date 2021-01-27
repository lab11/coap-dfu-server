FROM alpine:3

ENV PYTHONBUFFERED=1
ARG APP_PATH

WORKDIR /root/

RUN apk add --no-cache python3 && \
      python3 -m ensurepip && \
      pip3 install --no-cache --upgrade pip setuptools wheel

RUN pip3 install \
      watchdog \
      click \
      nrfutil \
      piccata

COPY coap-dfu-server.py coap-dfu-server.py

ENTRYPOINT ["python3", "coap-dfu-server.py", "-pkg ${APP_PATH}/_build/*.zip"]

