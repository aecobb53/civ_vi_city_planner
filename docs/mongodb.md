https://hub.docker.com/_/mongo

to pull this image run `docker pull mongo`
that will likely need to be in the setup

```yaml
# Use root/example as user/password credentials
version: '3.1'

services:

  mongo:
    image: mongo
    restart: always
    environment:
      MONGO_INITDB_ROOT_USERNAME: root
      MONGO_INITDB_ROOT_PASSWORD: example

  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 8081:8081
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: root
      ME_CONFIG_MONGODB_ADMINPASSWORD: example
```

Run docker stack deploy -c stack.yml mongo (or docker-compose -f stack.yml up), wait for it to initialize completely, and visit http://swarm-ip:8081, http://localhost:8081, or http://host-ip:8081 (as appropriate).

the above is how you run different docerk-compose files. maybe have a prod, dev, test docker-compose files
