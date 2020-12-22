from backend.common_tile import CommonTile
import math

from backend.districts.water_park import WaterPark
from backend.districts.entertainment_complex import EntertainmentComplex

class TheaterSquare(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'amphitheater',
            'archaeological_museum',
            'art_museum',
            'broadcast_center',
        ]
        self._building_list = None
        self._amphitheater = None
        self._archaeological_museum = None
        self._art_museum = None
        self._broadcast_center = None
        self._powered = None
        self._power = None
        self.specialist_yield = 2
        self.specialist_power_bonus = 1
        self.appeal = 1

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

    # amphitheater
    @property
    def amphitheater(self):
        if self._amphitheater is None:
            return None
        return self._amphitheater

    @amphitheater.setter
    def amphitheater(self, value):
        if value:
            self.culture = self.culture + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('amphitheater')
            self._amphitheater = True

    # archaeological_museum
    @property
    def archaeological_museum(self):
        if self._archaeological_museum is None:
            return None
        return self._archaeological_museum

    @archaeological_museum.setter
    def archaeological_museum(self, value):
        if value:
            self.culture = self.culture + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('archaeological_museum')
            self._archaeological_museum = True

    @archaeological_museum.deleter
    def archaeological_museum(self):
        if self._archaeological_museum:
            self.culture = self.culture - 2
            self.citizen_slot = self.citizen_slot - 1
            self.remove_building_list('archaeological_museum')
            self._archaeological_museum = False

    # art_museum
    @property
    def art_museum(self):
        if self._art_museum is None:
            return None
        return self._art_museum

    @art_museum.setter
    def art_museum(self, value):
        if value:
            self.culture = self.culture + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('art_museum')
            self._art_museum = True

    @art_museum.deleter
    def art_museum(self):
        if self._art_museum:
            self.culture = self.culture - 2
            self.citizen_slot = self.citizen_slot - 1
            self.remove_building_list('art_museum')
            self._art_museum = False

    # broadcast_center
    @property
    def broadcast_center(self):
        if self._broadcast_center is None:
            return None
        return self._broadcast_center

    @broadcast_center.setter
    def broadcast_center(self, value):
        if value:
            self.culture = self.culture + 4
            self.citizen_slot = self.citizen_slot + 1
            if self.powered:
                self.culture = self.culture + 4
                self.citizen_slot = self.citizen_slot + 1
                self.specialist_yield += self.specialist_power_bonus
            self.update_building_list('broadcast_center')
            self._broadcast_center = True

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
        self.power = 3
        self._powered = value

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement == None:
            self.powered = True
            final_improvement = 'broadcast_center'
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

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)

        adj_wonder = 0
        adj_water_part = 0
        adj_entertainment = 0
        adj_district = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if adj_obj.wonder is not None:
                adj_wonder += 1
            if adj_obj.district is not None:
                adj_district += 1 # TODO TEST THIS!! HERE
            if isinstance(adj_obj.district, WaterPark):
                adj_water_part += 1
            if isinstance(adj_obj.district, EntertainmentComplex):
                adj_entertainment += 1
        target_object.culture = target_object.culture + adj_wonder
        target_object.culture = target_object.culture + adj_water_part
        target_object.culture = target_object.culture + adj_entertainment
        target_object.culture = target_object.culture + math.floor(adj_district / 2)

    def calculate_specialist_yield(self):
        self.science = self.science + self.citizen_slot * self.specialist_yield
