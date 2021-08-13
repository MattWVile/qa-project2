#!bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:
ssh swarm-manager "export DATABASE_URI=${DATABASE_URI}"

ssh swarm-manager << EOF
    sudo usermod -aG docker $USER 
    docker login -u ${DOCKERHUB_CREDENTIALS_USR} -P ${DOCKERHUB_CREDENTIALS_PSW} 
    docker stack deploy --compose-file docker-compose.yaml make_meal 
EOF