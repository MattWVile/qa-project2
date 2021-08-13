#!bin/bash

rsync -r docker-compose.yaml nginx swarm-manager:

ssh swarm-manager << EOF
    "export DATABASE_URI=${DATABASE_URI} && export SECRET_KEY=${SECRET_KEY} && docker stack deploy --compose-file docker-compose.yaml Password"
    sudo usermod -aG docker $USER 
    docker login -u ${DOCKERHUB_CREDENTIALS_USR} -P ${DOCKERHUB_CREDENTIALS_PSW} 
    docker stack deploy --compose-file docker-compose.yaml make_meal 
EOF