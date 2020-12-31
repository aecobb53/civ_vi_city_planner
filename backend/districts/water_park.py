from backend.common_tile import CommonTile
import math


class WaterPark(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'ferris_wheel',
            'aquarium',
            'aquatics_center',
        ]
        self._building_list = None
        self._ferris_wheel = None
        self._aquarium = None
        self._aquatics_center = None
        self._powered = None
        self._power = None
        self.amenities = self.amenities + 1
        self.maintenance = self.maintenance + 1
        self.specialist_yield = 2
        self.specialist_power_bonus = 1

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

    # ferris_wheel
    @property
    def ferris_wheel(self):
        if self._ferris_wheel is None:
            return False
        return self._ferris_wheel

    @ferris_wheel.setter
    def ferris_wheel(self, value):
        if value:
            self.amenities = self.amenities + 1
            self.culture = self.culture + 3
            self.maintenance = self.maintenance + 1
            self.update_building_list('ferris_wheel')
            self._ferris_wheel = True

    # aquarium
    @property
    def aquarium(self):
        if self._aquarium is None:
            return False
        return self._aquarium

    @aquarium.setter
    def aquarium(self, value):
        if value:
            self.amenities = self.amenities + 1
            self.maintenance = self.maintenance + 2
            self.update_building_list('aquarium')
            self._aquarium = True

    # aquatics_center
    @property
    def aquatics_center(self):
        if self._aquatics_center is None:
            return False
        return self._aquatics_center

    @aquatics_center.setter
    def aquatics_center(self, value):
        if value:
            self.amenities = self.amenities + 1
            self.maintenance = self.maintenance + 3
            if self.powered:
                self.amenities = self.amenities + 2
            self.update_building_list('aquatics_center')
            self._aquatics_center = True

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
    def calculate_adjacency(self, tile_obj, target_index, adj_list):  # pragma: no cover
        pass

    def calculate_specialist_yield(self):
        pass
