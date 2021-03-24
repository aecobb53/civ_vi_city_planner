# New mongodb

To spin up the mongodb use `build reg` to spin up all reg instances. 
The docker-compose file runs this:

```yaml
    database:
        image: mongo
        restart: always
        ports:
            - 27017:27017
        # environment:
        #     MONGO_INITDB_ROOT_USERNAME: root
        #     MONGO_INITDB_ROOT_PASSWORD: example
```

The username/password are not needed but could be used. 
Because of docker-compose, all containers are already added to the same network. 

Here is an example of how to connect to the reg database from a test bash container:
```python
import pymongo

# host = 'localhost'
host = 'civ_vi_city_planner_database_1'
myclient = pymongo.MongoClient(f"mongodb://{host}:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st"},
  { "name": "Am2", "address": "Apple st2"},
  { "name": "Am3", "address": "Apple st3"}
]

x = mycol.insert_many(mylist)

print(x.inserted_ids)
```

Instead of hitting the localhost, you hit the hostname of the database. 
I dont know why the MongoClient needs "mongodb://" before the rest of the url but it appears to need it. 

## Query parameters

https://docs.mongodb.com/manual/reference/operator/query/


