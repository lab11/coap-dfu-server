FROM debian:10

ENV APP_PATH ${APP_PATH}
ARG REPO_URL
ARG GIT_SSH_KEY
ARG KEY_PATH
ARG DFU_PUBLIC_KEY_C
ARG DFU_PRIVATE_KEY

WORKDIR /root/

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
      git \
      wget \
      libprotobuf-dev \
      libprotoc-dev \
      protobuf-compiler \
      python3 \
      python3-pip \
      python3-protobuf

RUN  cd /tmp \
 && wget -c https://developer.arm.com/-/media/Files/downloads/gnu-rm/9-2020q2/gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 \
 && tar xjf gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 \
 && mv gcc-arm-none-eabi-9-2020-q2-update /opt/gcc-arm-none-eabi-9-2020-q2-update \
 && rm gcc-arm-none-eabi-9-2020-q2-update-x86_64-linux.tar.bz2 \
 && ln -s /opt/gcc-arm-none-eabi-9-2020-q2-update/bin/* /usr/local/bin/.

RUN pip3 install pip --upgrade

RUN pip3 install \
      nrfutil \
      piccata

RUN mkdir -p /root/.ssh
RUN echo "${GIT_SSH_KEY}" > /root/.ssh/id_dfu_server \
    && chmod 600 /root/.ssh/id_dfu_server
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
RUN eval $(ssh-agent -s) && \
      ssh-add /root/.ssh/id_dfu_server && \
      git clone --recursive ${REPO_URL}

RUN echo "${DFU_PUBLIC_KEY_C}" > ${KEY_PATH}/public.c
RUN echo "${DFU_PRIVATE_KEY}"  > ${KEY_PATH}/private.pem

COPY coap-dfu-server.py coap-server-dfu.py
