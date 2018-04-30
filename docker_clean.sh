docker stack rm hcmc
docker stack rm pyhello
docker rm $(docker ps --all --quiet) --force
#docker volume rm $(docker volume ls --quiet)