#!/bin/bash

set -e 

sudo apt-get update
sudo apt-get install curl jq -y

sudo apt-get-repository -y --update ppa:ansible/ansible
sudo apt-get install -y ansible

if [ -z "$(docker --version 2> /dev/null)" ]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $USER
fi

if [ -z "$(docker-compose --version 2> /dev/null)" ]; then
    sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
fi

