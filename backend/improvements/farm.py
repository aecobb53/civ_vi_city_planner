from common_tile import CommonTile
import math

class Farm(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.production = 0
        self.gold = 0
        self.houseing = .5
        self.acceptable_terrain = [
            'grassland',
            'plains',
        ]
        self.acceptable_features = [
            'floodplains',
            'volcanic_soil'
        ]
        self.resources = [
            'wheat',
            'rice',
            'maize',
        ]
        self.hills = True

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)
        adj_count = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if isinstance(adj_obj.improvement, Farm):
                adj_count += 1
        if tile_obj.erah >= 2:
            target_object.food = target_object.food + math.floor(adj_count / 2)
        if tile_obj.erah >= 5:
            target_object.food = target_object.food + adj_count
