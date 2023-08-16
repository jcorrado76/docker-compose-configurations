# Postgres

This subfolder is about how to run a local postgres instance.

This docker compose file uses the image from [here](https://hub.docker.com/r/bitnami/postgresql).

## Save your Database Data

To persist your database data, you need to mount a directory at the `/bitnami/postgresql` path, like this:

```yaml
services:
  postgresql:
  ...
    volumes:
      - /path/to/postgresql-persistence:/bitnami/postgresql
```

## Docker Networking

Docker provides really good [container networking support](https://docs.docker.com/network/), which allows you to communicate to other containers that are communicating over the same network. Using the docker network that gets created, you can communicate with other containers by just using the container name as the host name.

To create a network (these are called **bridge** networks), and attach your container to that network, you'd run:

```yaml
version: '2'

networks:
  app-tier:
    driver: bridge

services:
  postgresql:
    image: 'bitnami/postgresql:latest'
    networks:
      - app-tier

  myapp:
    image: 'myapp:latest'
    networks:
      - app-tier
```

## Initialize Data with SQL

When the container is executed, it will execute bash files found in `/docker-entrypoint-initdb.d` before initializing or starting postgresql.

So you can mount your custom files at that location as a volume.

When the container is executed **for the first time**, it will execute files with extensions `.sh`, `.sql` and `.sql.gz` located at `/docker-entrypoint-initdb.d`.

If you have flags you want to pass to the `postgres` startup command, you can do that by setting the `POSTGRESQL_EXTRA_FLAGS` environment variable.

## Setting Credentials

You can set the password and username for the postgres database by setting the environment variables:

```yaml
services:
  postgresql:
  ...
    environment:
      - POSTGRESQL_USERNAME=my_user
      - POSTGRESQL_PASSWORD=password123
      - POSTGRESQL_DATABASE=my_database
```
