import json
import os

from common_tile import CommonTile

class Farm(CommonTile):

    def __init__(
        self,
        erah=None):
        super().__init__()
        # self.food = 2
        # self.production = 1 if hills == True else 0
        # self.gold = 0

        self._food = None
        self._housing = None
        self._erah = None
        self.acceptable_terrain = []
        self.acceptable_features = []

    @property
    def food(self):
        if self.erah == None:
            return 1
        if self.erah < 2:
            return 1
        # elif self.erah >= 2 and self.erah < 5:
        #     return 2
        # elif self.erah >= 5:
        #     return 3
        else:
            return 1
