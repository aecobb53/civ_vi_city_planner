from backend.common_tile import CommonTile
from backend.features.reef import Reef
from backend.improvements.fishing_boats import FishingBoats

class Seastead(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 2
        self.houseing = 2
        self.acceptable_terrain = [
            'lake',
            'coast',
            'ocean',
        ]

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)
        adj_fishing_boat = 0
        adj_reef = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if isinstance(adj_obj.improvement, FishingBoats):
                adj_fishing_boat += 1
            if isinstance(adj_obj.improvement, Reef):
                adj_reef += 1
        target_object.production = target_object.production + adj_fishing_boat
        target_object.culture = target_object.culture + adj_reef
        target_object.tourism = target_object.tourism + adj_reef
