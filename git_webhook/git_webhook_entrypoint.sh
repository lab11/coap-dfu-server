#!/bin/sh

eval $(ssh-agent)
ssh-add /root/.ssh/id_dfu_server
/usr/bin/supervisord
