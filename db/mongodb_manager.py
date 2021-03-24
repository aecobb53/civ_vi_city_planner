import pymongo
import json
import yaml
import os
import re

class Database:

    def __init__(self, hostname='prod_host'):
        with open('etc/mongodb.yml') as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)
        url = f"mongodb://{self.config['reg-host']}:27017/"
        # url = f"mongodb://{self.config[os.getenv('MONGO_HOST')]}:27017/"
        print(url)

        print(json.dumps(self.config, indent=2))
        self._client = pymongo.MongoClient(url)
        self._mydb = self._client["mydatabase"]

    def populate_database(self, collection, data):
        col = self._mydb[collection]
        if not isinstance(data, list):
            data = list(data)
        message = col.insert_many(data)
        print(message)

    def return_from_database(self, collection, parameters={}):
        col = self._mydb[collection]
        data = col.find(parameters)
        for i in data:
            print(i)
        return data

    def remove_from_database(self, collection, parameters=None):
        if parameters is None:
            return
        col = self._mydb[collection]
        data = col.delete_many(parameters)
        print(data)

    def list_collections(self):
        col_list = self._mydb.list_collections()
        for col in col_list:
            print(col)
        return col_list

if __name__ == '__main__':
    DB = Database()

    mylist = [
        { "name": "Amy", "address": "Apple st"},
        { "name": "Am2", "address": "Apple st2"},
        { "name": "Am3", "address": "Apple st3"}
    ]

    print('amy search')
    DB.return_from_database('cities', { "name": { "$regex": "^Am" } })

    # DB.return_from_database('cities')
    DB.populate_database('cities', mylist)
    # DB.return_from_database('cities')
    print('amy search')
    DB.return_from_database('cities', { "name": { "$regex": "^Am" } })
    print('amy delete')
    DB.remove_from_database('cities', { "name": { "$regex": "^Am\d" } })
    print('amy search')
    DB.return_from_database('cities', { "name": { "$regex": "^Am" } })

    # DB.list_collections()
