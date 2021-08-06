#!/bin/bash

set -e 

sudo apt-get update
sudo apt-get install curl jq -y

if [ -z "$(docker --version 2> /dev/null)" ]; then
    curl https://get.docker.com | sudo bash
    sudo usermod -aG docker $USER
fi
