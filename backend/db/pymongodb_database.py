import pymongo
import json
import yaml
import os
import re

class PymongoDBDatabase:

    def __init__(self, database_name, collection):
        with open('etc/mongodb.yml') as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)['mongodb']
        url = f"mongodb://{self.config['host']}:27017/"

        self._client = pymongo.MongoClient(url)
        self._mydb = self._client[database_name]
        self._collection = self._mydb[collection]

    def write_to_database(self, data):
        message = self._collection.insert_many(data)
        return message

    def find_in_database(self, parameters):
        data = self._collection.find(parameters)
        return data

    def remove_from_database(self, parameters):
        data = self._collection.delete_many(parameters)
        return data

    def list_database_collections(self):
        col_list = self._mydb.list_collections()
        return col_list

# if __name__ == '__main__':
#     DB = PymongoDBDatabase('civ_vi_prod', 'cities')

#     mylist = [
#         { "name": "Amy", "address": "Apple st"},
#         { "name": "Am2", "address": "Apple st2"},
#         { "name": "Am3", "address": "Apple st3"}
#     ]

#     print('amy search')
#     DB.find_in_database({ "name": { "$regex": "^Am" } })

#     # # DB.find_in_database('cities')
#     # DB.write_to_database(mylist)
#     # # DB.find_in_database('cities')
#     # print('amy search')
#     # DB.find_in_database({ "name": { "$regex": "^Am" } })
#     # print('amy delete')
#     # DB.remove_from_database({ "name": { "$regex": "^Am\d" } })
#     # print('amy search')
#     # DB.find_in_database({ "name": { "$regex": "^Am" } })

#     # # DB.list_database_collections()
