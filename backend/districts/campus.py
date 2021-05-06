from backend.common_tile import CommonTile
import math

from backend.features.mountain import Mountain
from backend.features.rainforest import Rainforest
from backend.features.geothermal_fissure import GeothermalFissure
from backend.features.reef import Reef


class Campus(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'library',
            'university',
            'research_lab',
        ]
        self._building_list = None
        self._library = None
        self._university = None
        self._research_lab = None
        self._powered = None
        self._power = None
        self.maintenance = self.maintenance + 1
        self.specialist_yield = 2
        self.specialist_bonus = 1

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

    # library
    @property
    def library(self):
        if self._library is None:
            return False
        return self._library

    @library.setter
    def library(self, value):
        if value:
            self.science = self.science + 2
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 1
            self.update_building_list('library')
            self._library = True

    # university
    @property
    def university(self):
        if self._university is None:
            return False
        return self._university

    @university.setter
    def university(self, value):
        if value:
            self.science = self.science + 4
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 2
            self.update_building_list('university')
            self._university = True

    # research_lab
    @property
    def research_lab(self):
        if self._research_lab is None:
            return False
        return self._research_lab

    @research_lab.setter
    def research_lab(self, value):
        if value:
            self.science = self.science + 3
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 3
            if self.powered:
                self.science = self.science + 5
            self.specialist_yield += self.specialist_bonus
            self.update_building_list('research_lab')
            self._research_lab = True

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
        print(final_improvement, powered)

        if final_improvement is None:
            powered = True
            final_improvement = 'research_lab'
        try:
            final_improvement = int(final_improvement)
        except:
            pass
        if isinstance(final_improvement, int):
            final_improvement = self.default_building_list[final_improvement]

        if powered:
            print('powered if run')
            print(self.powered)
            self.powered = True
            print(self.powered)

        for building in self.default_building_list:
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_adjacency(self, tile_obj, target_index, adj_list):  # pragma: no cover
        print('adj calculated')
        target_object = getattr(tile_obj, target_index)

        adj_mountain = 0
        adj_rainforest = 0
        adj_geo_reef = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if isinstance(adj_obj.feature, Mountain):
                adj_mountain += 1
            if isinstance(adj_obj.feature, Rainforest):
                adj_rainforest += 1
            if isinstance(adj_obj.feature, GeothermalFissure) or isinstance(adj_obj.feature, Reef):
                adj_geo_reef += 1
        target_object.science = target_object.science + adj_mountain
        target_object.science = target_object.science + math.floor(adj_rainforest / 2)
        target_object.science = target_object.science + adj_geo_reef * 2

    def calculate_specialist_yield(self):
        print('special calculated')
        self.science = self.science + self.citizen_slot * self.specialist_yield
