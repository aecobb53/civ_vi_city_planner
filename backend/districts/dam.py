from backend.common_tile import CommonTile
import math

from backend.features.river import River

class Dam(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'hydroelectric_dam',
        ]
        self._building_list = None
        self._hydroelectric_dam = None
        self._powered = None
        self._power = None
        self.housing = self.housing + 3
        self.appeal = 1

    # building_list
    @property
    def building_list(self):
        if self._building_list is None:
            return None
        return self._building_list

    # @building_list.setter
    def update_building_list(self, value):
        if self._building_list is None:
            self._building_list = []
        self._building_list.append(value)

    def remove_building_list(self, value):
        if self._building_list is None:
            return None
        self._building_list.remove(value)

    # hydroelectric_dam
    @property
    def hydroelectric_dam(self):
        if self._hydroelectric_dam is None:
            return False
        return self._hydroelectric_dam

    @hydroelectric_dam.setter
    def hydroelectric_dam(self, value):
        if value:
            self.maintenance = self.maintenance + 1
            self.update_building_list('hydroelectric_dam')
            self._hydroelectric_dam = True

    # power - Whats the power draw
    @property
    def power(self):
        if self._power is None:
            return 0
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    # powered - Does the city need power?
    @property
    def powered(self):
        if self._powered is None:
            return False
        return self._powered

    @powered.setter
    def powered(self, value):
        self.power = 0
        self._powered = value

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement == None:
            self.powered = True
            final_improvement = 'hydroelectric_dam'
        if final_improvement == 'hydroelectric_dam' and powered is None:
            powered = True
        try:
            final_improvement = int(final_improvement)
        except:
            pass
        if isinstance(final_improvement, int):
            final_improvement = self.default_building_list[final_improvement]

        if powered:
            self.powered = True

        for building in self.default_building_list:
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_adjacency(self, tile_obj, target_index, adj_list):  # pragma: no cover
        """
        I dont know if removing a dam from the orig object like this will actually work... 
        if it doesnt it needs to be taken care of in another method
        """
        target_object = getattr(tile_obj, target_index)

        adj_river = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if isinstance(adj_obj.district, River):
                adj_river += 1
        if adj_river < 2:
            target_object.district = None

    def calculate_specialist_yield(self):
        pass
