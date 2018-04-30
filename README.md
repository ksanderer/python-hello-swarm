Here you can find a very basic example how to use [docker swarm config](https://docs.docker.com/compose/compose-file/#configs) and [healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck) feature.

## Setup
#### Build image
```
docker build -t pyhello .
```

#### Run image in a single host mode
```
docker run -t -p 8000:8000 pyhello:latest
```

Open your browser at `http://localhost:8000`
You should see `Hello world!`

#### Init swarm
```
docker swarm init
```

#### Deploy stack
```
 docker stack deploy --compose-file compose/stack-compose.yaml pyhello
```

Open your browser at `http://localhost:8000`
You should see `Hello Swarm Config!` sourced from the swarm config file.


