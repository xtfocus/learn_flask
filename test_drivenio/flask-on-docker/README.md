# Learn things about docker and docker volume

https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/#project-setup

Example docker-compose file


```
# docker-compose.yml

version: '3.8'

services:
  web:
    build: ./services/web # where to find Dockerfile
    command: python manage.py run -h 0.0.0.0
    volumes:
      - ./services/web/:/usr/src/app/ # bind mounts
    ports:
      - 5001:5000
    env_file:
      - ./.env.dev
    depends_on:
      - db
  db:
    image: postgres:13
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_USER=hello_flask
      - POSTGRES_PASSWORD=hello_flask
      - POSTGRES_DB=hello_flask_dev

volumes:
  # named volume
  postgres_data:
```

## Bind mounts

This is used in the `web` service. The line 
```
- ./services/web/:/usr/src/app/

```
in the volumes section under `web` is a bind mount. Here, \
`./services/web/`\
is the path to the directory on the **host machine**, and \
`/usr/src/app/`\
is the path where the volume is mounted in the container. Any changes made to the files in the `./services/web/` directory on the host will be reflected in the `/usr/src/app/` directory inside the container.

## Named volumes

This is used in the `db` service. The line 
```
- postgres_data:/var/lib/postgresql/data/ 
```
in the volumes section under `db` is a named volume. Here, `postgres_data` is the name of the volume, and `/var/lib/postgresql/data/` is the path where the volume is mounted in the container. 

>Named volumes are a type of Docker-managed volume that persist data across container lifecycles. The postgres_data volume is also declared at the bottom of the Docker Compose file under the volumes key. This volume stores the database data and ensures that it persists even if the db container is stopped or deleted

## The difference

`./services/web/` directory is a directory on your host machine.

`postgres_data` is a named volume managed by Docker. The data in a named volume is stored in a part of your host file system which Docker manages (usually `/var/lib/docker/volumes/` on Linux systems). While it’s technically on your host machine, it’s not meant to be accessed directly.


__________
**Question**: What happen if
```
volumes:
  postgres_data:
```
is not there?

**Answer**: 
Docker will still create a volume for the `db` service because it’s specified in the volumes: section under the `db` service. However, this volume will not be a named volume, but an anonymous volume.

>An anonymous volume is similar to a named volume but it’s given a random name by Docker, making it harder to reference in the future. Anonymous volumes are not listed under the `docker volume ls` command, which makes them harder to manage.
__________

**Question**: What if a directory named `postgres_data` exists on the host machine and 
```
volumes:
  postgres_data:
```

is not in the `docker-compose.yml`? Does it create a bind mount?

**Answer**: No, if you want to create a bind mount using the directory `postgres_data`, do
```
db:
  ...
  volumes:
    - ./postgres_data:/var/lib/postgresql/data/
  ...
```
Otherwise, Docker will still create an anonymous volume.
__________
**Question**: Advantage of named volumes?
**Answer**:

Named volumes, like `postgres_data` in your docker-compose.yml file, have several advantages:

  - Persistence: Data in named volumes persists even if the container itself is deleted. This is particularly useful for databases, where you want to keep the data safe even if the container crashes or is removed.

  - Portability: Named volumes can be easily backed up and transferred between different machines, making your application more portable.

  - Management: Docker provides commands to manage named volumes, making it easier to create, delete, or get information about the volume.

  - Isolation: Named volumes are isolated from the host file system and are managed by Docker. This can provide an additional layer of security and abstraction.

  - Compatibility: Named volumes work consistently across different platforms and environments, whereas the behavior of bind mounts can vary.



