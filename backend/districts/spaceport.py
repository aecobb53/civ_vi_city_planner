from backend.common_tile import CommonTile
import math


class Spaceport(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = []
        self.appeal = self.appeal - 1
        self._building_list = None

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):
        pass

    # building_list
    @property
    def building_list(self):
        if self._building_list is None:
            return None
        return self._building_list

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        pass

    def calculate_specialist_yield(self):
        pass
