import json
import yaml
import math
import uuid

from backend.common_tile import CommonTile
from backend.tile_container import Tile
from backend.terrain import *
from backend.features import *
from backend.improvements import *
from backend.districts import *
from backend.resources import *

# Config
with open('etc/backend.yml') as ycf:
    config = yaml.load(ycf, Loader=yaml.FullLoader)

class TileValidator:

    def __init__(self, tile):
        print(tile)


tile = []
tile.append('')
TV = TileValidator()