from backend.common_tile import CommonTile
import math

from backend.districts.city_center import CityCenter
from backend.terrain.coast import Coast
from backend.terrain.ocean import Ocean


class Harbor(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'lighthouse',
            'shipyard',
            'seaport',
        ]
        self._building_list = None
        self._lighthouse = None
        self._shipyard = None
        self._seaport = None
        self._powered = None
        self._power = None
        self.specialist_gold_yield = 2
        self.specialist_food_yield = 1

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

    # lighthouse
    @property
    def lighthouse(self):
        if self._lighthouse is None:
            return False
        return self._lighthouse

    @lighthouse.setter
    def lighthouse(self, value):
        if value:
            self.food = self.food + 1
            self.gold = self.gold + 1
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('lighthouse')
            self._lighthouse = True

    # shipyard
    @property
    def shipyard(self):
        if self._shipyard is None:
            return False
        return self._shipyard

    @shipyard.setter
    def shipyard(self, value):
        if value:
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 2
            self.update_building_list('shipyard')
            self._shipyard = True

    # seaport
    @property
    def seaport(self):
        if self._seaport is None:
            return False
        return self._seaport

    @seaport.setter
    def seaport(self, value):
        if value:
            self.food = self.food + 2
            self.gold = self.gold + 2
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_food_yield += 1
            self.update_building_list('seaport')
            self._seaport = True

    # power - Whats the power draw
    @property
    def power(self):
        if self._power is None:
            return 0
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
            final_improvement = 'seaport'
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

        adj_city_center = 0
        adj_sea = 0
        adj_districts = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if adj_obj.district is not None:
                adj_district += 1 # TODO TEST THIS!! HERE
            if isinstance(adj_obj.district, CityCenter):
                adj.city_center += 1
            if isinstance(adj_obj.terrain, Coast) or isinstance(adj_obj.terrain, Ocean):
                adj_sea += 1
        target_object.gold = target_object.gold + (adj_city_center * 2)
        target_object.gold = target_object.gold + adj_sea
        target_object.gold = target_object.gold + math.floor(adj_district / 2)
        if self.seaport:
            self.production = self.production + (\
                (adj_city_center * 2) + \
                adj_sea + \
                math.floor(adj_district / 2))

    def calculate_specialist_yield(self):
        self.gold = self.gold + self.citizen_slot * self.specialist_gold_yield
        self.food = self.food + self.citizen_slot * self.specialist_food_yield
