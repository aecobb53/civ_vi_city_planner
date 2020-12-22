from backend.common_tile import CommonTile
import math
# from features.mountain import Mountain
# from features.rainforest import Rainforest
# from features.geothermal_fissure import GeothermalFissure
# from features.reef import Reef
from districts.water_park import WaterPark
from districts.entertainment_complex import EntertainmentComplex

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
        if value is True:
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
        if value is True:
            self.culture = self.culture + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('archaeological_museum')
            self._archaeological_museum = True

    @archaeological_museum.deleter
    def archaeological_museum(self):
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
        if value is True:
            self.culture = self.culture + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('art_museum')
            self._art_museum = True

    @art_museum.deleter
    def art_museum(self):
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
        if value is True:
            self.culture = self.culture + 4
            self.citizen_slot = self.citizen_slot + 1
            if self.powered:
                self.culture = self.culture + 4
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('broadcast_center')
            self._broadcast_center = True
            # Building details
            pass

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

    # def calculate_adjacency(self, tile_obj, target_index, adj_list):
    #     target_object = getattr(tile_obj, target_index)

    #     adj_mountain = 0
    #     adj_rainforest = 0
    #     adj_geo_reef = 0
    #     for adj_obj in adj_list:
    #         if adj_obj is None:
    #             continue
    #         if isinstance(adj_obj.feature, Mountain):
    #             adj_mountain += 1
    #         if isinstance(adj_obj.feature, Rainforest):
    #             adj_rainforest += 1
    #         if isinstance(adj_obj.feature, GeothermalFissure) or isinstance(adj_obj.feature, Reef):
    #             adj_geo_reef += 1
    #     target_object.science = target_object.science + adj_mountain
    #     target_object.science = target_object.science + math.floor(adj_rainforest / 2)
    #     target_object.science = target_object.science + adj_geo_reef
