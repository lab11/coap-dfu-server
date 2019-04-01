#!/bin/bash

# setup coap dfu server service
sudo cp services/coap-dfu-server.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable coap-dfu-server
sudo systemctl start coap-dfu-server

# set up git deployment
mkdir /home/ubuntu/permamote
git init --bare /home/ubuntu/permamote.git

cp hooks/post-receive /home/ubuntu/permamote.git/hooks
