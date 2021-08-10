#!/bin/bash

set -e 

sudo apt-get update
sudo apt-get install curl jq -y

if [ -z "$(docker --version 2> /dev/null)" ]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $USER
    curl https://get.docker.com | sudo bash
    sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi
