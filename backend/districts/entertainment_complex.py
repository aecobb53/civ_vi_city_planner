from backend.common_tile import CommonTile
import math


class EntertainmentComplex(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'arena',
            'zoo',
            'stadium',
        ]
        self._building_list = None
        self._arena = None
        self._zoo = None
        self._stadium = None
        self._powered = None
        self._power = None
        self.specialist_yield = 2
        self.specialist_power_bonus = 1

    # building_list
    @property
    def building_list(self):
        if self._building_list == None:
            return None
        return self._building_list

    # @building_list.setter
    def update_building_list(self, value):
        if self._building_list == None:
            self._building_list = []
        self._building_list.append(value)

    # arena
    @property
    def arena(self):
        if self._arena is None:
            return None
        return self._arena

    @arena.setter
    def arena(self, value):
        if value:
            self.amenities = self.amenities + 1
            self.update_building_list('arena')
            self._arena = True

    # zoo
    @property
    def zoo(self):
        if self._zoo is None:
            return None
        return self._zoo

    @zoo.setter
    def zoo(self, value):
        if value:
            self.amenities = self.amenities + 1
            self.update_building_list('zoo')
            self._zoo = True

    # stadium
    @property
    def stadium(self):
        if self._stadium is None:
            return None
        return self._stadium

    @stadium.setter
    def stadium(self, value):
        if value:
            self.amenities = self.amenities + 1
            if self.powered:
                self.amenities = self.amenities + 2
            self.update_building_list('stadium')
            self._stadium = True


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
        self.power = 2
        self._powered = value

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement is None:
            powered = True
            final_improvement = 'stadium'
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
