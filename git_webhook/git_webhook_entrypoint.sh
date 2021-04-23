#!/bin/sh

eval $(ssh-agent)
ssh-add /root/.ssh/id_dfu_server
python3 git_webhook_server.py
