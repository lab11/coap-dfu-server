#!/bin/sh

eval $(ssh-agent)
ssh-add /root/.ssh/id_dfu_server
python3 dfu-webhook-endpoint.py
