

import json
import yaml
import os
import re


from backend.db.pymongodb_database import PymongoDBDatabase


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
