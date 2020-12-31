from backend.common_tile import CommonTile
import math


class DiplomaticQuarter(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'consulate',
            'chancery',
        ]
        self._building_list = None
        self._consulate = None
        self._chancery = None
        self._powered = None
        self._power = None
        self.maintenance = self.maintenance + 1

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

    #consulate
    @property
    def consulate(self):
        if self._consulate is None:
            return False
        return self._consulate
    
    @consulate.setter
    def consulate(self, value):
        if value:
            self.maintenance = self.maintenance + 1
            self.update_building_list('consulate')
            self._consulate = True

    #chancery
    @property
    def chancery(self):
        if self._chancery is None:
            return False
        return self._chancery
    
    @chancery.setter
    def chancery(self, value):
        if value:
            self.maintenance = self.maintenance + 2
            self.update_building_list('chancery')
            self._chancery = True

    # power - Whats the power draw
    @property
    def power(self):
        if self._power is None:
            return False
        return self._power

    @power.setter
    def power(self, value):
        pass
        # self._power = value

    # powered - Does the city need power?
    @property
    def powered(self):
        if self._powered is None:
            return False
        return self._powered

    @powered.setter
    def powered(self, value):
        # self.power = 3
        # self._powered = value
        pass

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement is None:
            powered = True
            final_improvement = 'chancery'
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
        pass

    def calculate_specialist_yield(self):
        pass
