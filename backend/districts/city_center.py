from backend.common_tile import CommonTile

class CityCenter(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'monument',
            'granary',
            'water_mill',
            'sewer',
            'flood_barrier',
            'ancient_walls',
            'medival_walls',
            'renaissance_walls',
        ]
        self._building_list = None
        self._monument = None
        self._granary = None
        self._water_mill = None
        self._sewer = None
        self._flood_barrier = None
        self._ancient_walls = None
        self._medival_walls = None
        self._renaissance_walls = None
        self._powered = None
        self._power = None

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

    def remove_building_list(self, value):
        if self._building_list == None:
            return None
        self._building_list.remove(value)

    # monument
    @property
    def monument(self):
        if self._monument is None:
            return None
        return self._monument

    @monument.setter
    def monument(self, value):
        if value:
            self.culture = self.culture + 2
            self.update_building_list('monument')
            self._monument = True

    # granary
    @property
    def granary(self):
        if self._granary is None:
            return None
        return self._granary

    @granary.setter
    def granary(self, value):
        if value:
            self.food = self.food  + 1
            self.housing = self.houseing  + 2
            self.update_building_list('granary')
            self._granary = True

    # water_mill
    @property
    def water_mill(self):
        if self._water_mill is None:
            return None
        return self._water_mill

    @water_mill.setter
    def water_mill(self, value):
        if value:
            self.food = self.food + 1
            self.production = self.production + 1
            self.update_building_list('water_mill')
            self._water_mill = True
            # extra food per bonus resource and must be next to river

    @water_mill.deleter
    def water_mill(self):
        if self._water_mill:
            self.food = self.food - 1
            self.production = self.production - 1
            self.remove_building_list('water_mill')
            self._water_mill = None

    # sewer
    @property
    def sewer(self):
        if self._sewer is None:
            return None
        return self._sewer

    @sewer.setter
    def sewer(self, value):
        if value:
            self.houseing = self.houseing + 2
            self.update_building_list('sewer')
            self._sewer = True

    # flood_barrier
    @property
    def flood_barrier(self):
        if self._flood_barrier is None:
            return None
        return self._flood_barrier

    @flood_barrier.setter
    def flood_barrier(self, value):
        if value:
            self.update_building_list('flood_barrier')
            self._flood_barrier = True

    # ancient_walls
    @property
    def ancient_walls(self):
        if self._ancient_walls is None:
            return None
        return self._ancient_walls

    @ancient_walls.setter
    def ancient_walls(self, value):
        if value:
            self.update_building_list('ancient_walls')
            self._ancient_walls = True

    # medival_walls
    @property
    def medival_walls(self):
        if self._medival_walls is None:
            return None
        return self._medival_walls

    @medival_walls.setter
    def medival_walls(self, value):
        if value:
            self.update_building_list('medival_walls')
            self._medival_walls = True

    # renaissance_walls
    @property
    def renaissance_walls(self):
        if self._renaissance_walls is None:
            return None
        return self._renaissance_walls

    @renaissance_walls.setter
    def renaissance_walls(self, value):
        if value:
            self.update_building_list('renaissance_walls')
            self._renaissance_walls = True

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

    def set_buildings(self, final_improvement=None, powered=None):

        if final_improvement == None:
            # self.powered = True
            final_improvement = 'flood_barrier'
        try:
            final_improvement = int(final_improvement)
        except:
            pass
        if isinstance(final_improvement, int):
            final_improvement = self.default_building_list[final_improvement]

        for building in self.default_building_list:
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)

        if not target_object.river:
            if self.water_mill:
                del self.water_mill
