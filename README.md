## `Docker Compose Setup`

This repository contains a Docker Compose setup for a multi-container application consisting of Redis, Redis Insight, and a Core API.

Prerequisites
Make sure you have Docker and Docker Compose installed on your system.

* [Docker Installation Guide](https://docs.docker.com/get-docker/)
* [Docker Compose Installation Guide](https://docs.docker.com/compose/install/)

## Setup
Unzip this repository to your local machine:

Set up environment variables:

* Create a .env file in the root directory of this project.
* Define environment variables following the .env.example file format.
* Run the following command to start the services:

bash
```
docker-compose up -d
```
In order to restart the containers and reset the environment, you can run the
following command from the project root directory:


`$ docker compose down -v && docker compose up -d --build --force-recreate`

This will stop the containers, remove the volumes and start the containers
again.

## Stopping the containers
To stop the containers, you can use the command `docker compose down` from the same directory as the `docker-compose.yml`. Using this command, however, will only stop the machine and will not destroy the volume that was created with it.
To clean the volume as well, use the -v parameter as 

```docker compose down -v```

Access the services:

```
Redis: Accessible at localhost:6379.
Redis Insight: Accessible at localhost:8001.
Core API: Accessible at localhost:8000.
```

