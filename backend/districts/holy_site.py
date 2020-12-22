from backend.common_tile import CommonTile
import math

from backend.features.mountain import Mountain
from backend.features.rainforest import Woods


class HolySite(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'shrine',
            'temple',
        ]
        self._building_list = None
        self._shrine = None
        self._temple = None
        self._powered = None
        self._power = None
        self.specialist_yield = 2

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

    # shrine
    @property
    def shrine(self):
        if self._shrine is None:
            return None
        return self._shrine

    @shrine.setter
    def shrine(self, value):
        if value:
            self.faith = self.faith + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('shrine')
            self._shrine = value

    # temple
    @property
    def temple(self):
        if self._temple is None:
            return None
        return self._temple

    @temple.setter
    def temple(self, value):
        if value:
            self.faith = self.faith + 4
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('temple')
            self._temple = value

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
            final_improvement = 'temple'
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

        adj_natural_wonder = 0
        adj_mountain = 0
        adj_woods = 0
        adj_district = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            # if adj_obj.natural_wonder is not None:
            #     adj_wonder += 1
            # if adj_obj.district is not None:
            #     adj_woods += 1 # TODO TEST THIS!! HERE
            # This one above only applies if the woods is unimproved
            if isinstance(adj_obj.feature, Mountain):
                adj_mountain += 1
            if isinstance(adj_obj.feature, Woods):
                adj_mountain += 1
            if isinstance(adj_obj.feature, GeothermalFissure) or isinstance(adj_obj.feature, Reef):
                adj_geo_reef += 1
        target_object.science = target_object.science + adj_natural_wonder * 2
        target_object.science = target_object.science + adj_mountain
        target_object.culture = target_object.culture + math.floor(adj_district / 2)


    def calculate_specialist_yield(self):
        self.science = self.science + self.citizen_slot * self.specialist_yield
