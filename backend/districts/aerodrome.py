from backend.common_tile import CommonTile
import math


class Aerodrome(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'hanger',
            'airport',
        ]
        self._building_list = None
        self._hanger = None
        self._airport = None
        self._powered = None
        self._power = None
        self.appeal = self.appeal - 1
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

    # hanger
    @property
    def hanger(self):
        if self._hanger is None:
            return False
        return self._hanger

    @hanger.setter
    def hanger(self, value):
        if value:
            self.production = self.production + 2
            self.maintenance = self.maintenance + 1
            self.update_building_list('hanger')
            self._hanger = True

    # airport
    @property
    def airport(self):
        if self._airport is None:
            return False
        return self._airport

    @airport.setter
    def airport(self, value):
        if value:
            self.production = self.production + 4
            self.maintenance = self.maintenance + 2
            if self.powered:
                self.production = self.production + 2
            self.update_building_list('airport')
            self._airport = True

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
        self.power = 1
        self._powered = value

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement is None:
            powered = True
            final_improvement = 'airport'
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
