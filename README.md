COAP DFU Server for Nordic Secure DFU
=====================================

A cloud-based DFU server for devices using Nordic's secure DFU process. Based
on the DFU server in
[pc-nrfutil](https://github.com/NordicSemiconductor/pc-nrfutil).

Utilizes git webhooks for deployment.


### Docker support
This service is built as a docker image. Assumes a deployment key is created
for a repo. Need to generate keys for image signing/verification with `nrfutil`.

To build:
```
sudo docker-compose build \
       --build-arg GIT_SSH_KEY="$(cat <path to deploy ssh key>)" \
       --build-arg DFU_PUBLIC_KEY_C="$(cat <path to public.c>)" \
       --build-arg DFU_PRIVATE_KEY="$(cat <path to private.pem>)"
```

Configure the docker image with variables in `.env`.
