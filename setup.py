#!/usr/bin/python
import os
import yaml
import json
import requests


class SetupWeatherman:

    def __init__(self):
        # Load config file and set some parameters
        self.master_config = 'etc/backend.yml'
        with open(self.master_config) as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)

    # Setting up directories
    def verify_directories(self):
        """
        Verify the list of directores exists
        """
        for directory in self.config['verify_directories']:
            # print(directory)
            if not os.path.exists(directory):
                os.makedirs(directory)

if __name__ == '__main__':
    print('its the main app so its should run the full setup')