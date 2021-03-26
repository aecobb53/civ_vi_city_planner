

import json
import yaml
import os
import re


# from pymongodb_databse import PymongoDBDatabase


class CivVIDatabase:

    def __init__(self):
        with open('etc/mongodb.yml') as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)['civ_database']
        self.cities_db = PymongoDBDatabase('civ_vi_' + os.getenv('MONGOENV'), 'cities')

    def write_to_cities_database(self, data):
        if not isinstance(data, list):
            data = [data]
        output = self.cities_db.write_to_database(data)
        return output

    def find_in_cities_database(self, parameters):
        output = self.cities_db.find_in_database(parameters)
        if output is None:
            return []
        return output

    def remove_from_cities_database(self, parameters):
        output = self.cities_db.remove_from_database(parameters)
        return output
    # def list_database_collections(self):

if __name__ == '__main__':
    print('running this thing')
    CD = CivVIDatabase()
    print('database dump')
    for i in CD.find_in_cities_database({}):
        print(i)

    testdata = {
        'name': 'Andrew',
        'details': 'string'
    }

    print(CD.write_to_cities_database(testdata))

    for i in CD.find_in_cities_database({}):
        print(i)

    testdata = [
        {'name': 'Andrew','details': 'string'},
        {'name': 'Andrew','details': 'string'}
    ]

    print(CD.write_to_cities_database(testdata))

    for i in CD.find_in_cities_database({}):
        print(i)

    print(CD.remove_from_cities_database({}))

    for i in CD.find_in_cities_database({}):
        print(i)
