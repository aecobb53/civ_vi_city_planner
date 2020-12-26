from backend.common_tile import CommonTile
import math

from backend.terrain import Coast
from backend.terrain import Ocean
from backend.features import River


class Aqueduct(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = []
        self._building_list = None
        self.houseing = self.houseing + 2

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
        target_object = getattr(tile_obj, target_index)

        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if isinstance(adj_obj.terrain, (Coast, Ocean)) or isinstance(adj_obj, River):
                return None
        self.houseing = self.houseing + 4

    def calculate_specialist_yield(self):
        pass
