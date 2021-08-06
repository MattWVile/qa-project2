#!/bin/bash

set -e

sudo apt-get update > /dev/null
sudo apt-get install python3 python3-venv libpq -y > /dev/null

python3 -m venv venv 
source venv/bin/activate
for num in {1..4}; do pip3 install -r service_${num}/requirements.txt > /dev/null; done

python3 -m pytest --cov --cov-config=.coveragec
