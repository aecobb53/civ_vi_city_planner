import json
import os

from .plains import Plains
from common_tile import CommonTile

class Grassland(CommonTile):
# class Grassland():

    def __init__(
        self,
        hills=None
    ):
        super().__init__()
        self.food = 2
        self.production = 1 if hills == True else 0
        self.gold = 0
