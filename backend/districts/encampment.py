from backend.common_tile import CommonTile
import math


class Encampment(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'barracks',
            'stable',
            'armory',
            'military_academy',
        ]
        self._building_list = None
        self._barracks = None
        self._stable = None
        self._armory = None
        self._military_academy = None
        self._powered = None
        self._power = None
        self.maintenance = self.maintenance + 1
        self.specialist_production_yield = 1
        self.specialist_gold_yield = 2
        self.specialist_power_bonus = 1
        self.appeal = self.appeal - 1

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

    def remove_building_list(self, value):
        if self._building_list is None:
            return None
        self._building_list.remove(value)

    # barracks
    @property
    def barracks(self):
        if self._barracks is None:
            return False
        return self._barracks

    @barracks.setter
    def barracks(self, value):
        if value:
            self.production = self.production + 1
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 1
            self.update_building_list('barracks')
            self._barracks = True
            if self.stable:
                del self.stable

    @barracks.deleter
    def barracks(self):
        if self._barracks:
            self.production = self.production - 1
            self.housing = self.housing - 1
            self.citizen_slot = self.citizen_slot - 1
            self.maintenance = self.maintenance - 1
            self.remove_building_list('barracks')
            self._barracks = None

    # stable
    @property
    def stable(self):
        if self._stable is None:
            return False
        return self._stable

    @stable.setter
    def stable(self, value):
        if value:
            self.production = self.production + 1
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 1
            self.update_building_list('stable')
            self._stable = True
            if self.barracks:
                del self.barracks

    @stable.deleter
    def stable(self):
        if self._stable:
            self.production = self.production - 1
            self.housing = self.housing - 1
            self.citizen_slot = self.citizen_slot - 1
            self.maintenance = self.maintenance - 1
            self.remove_building_list('stable')
            self._stable = None

    # armory
    @property
    def armory(self):
        if self._armory is None:
            return False
        return self._armory

    @armory.setter
    def armory(self, value):
        if value:
            self.production = self.production + 3
            self.citizen_slot = self.citizen_slot + 1
            self.maintenance = self.maintenance + 2
            self.update_building_list('armory')
            self._armory = True

    # military_academy
    @property
    def military_academy(self):
        if self._military_academy is None:
            return False
        return self._military_academy

    @military_academy.setter
    def military_academy(self, value):
        if value:
            self.production = self.production + 3
            self.housing = self.housing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_production_yield += self.specialist_power_bonus
            self.maintenance = self.maintenance + 2
            self.update_building_list('military_academy')
            self._military_academy = True

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
            final_improvement = 'military_academy'
        try:
            final_improvement = int(final_improvement)
        except:
            pass
        if isinstance(final_improvement, int):
            final_improvement = self.default_building_list[final_improvement]

        if powered:
            self.powered = True

        for building in self.default_building_list:
            # if final_improvement == 'stable' and building == 'barracks':
            #     continue
            # elif building == 'stable':

            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_adjacency(self, tile_obj, target_index, adj_list):  # pragma: no cover
        pass

    def calculate_specialist_yield(self):
        self.production = self.production + self.citizen_slot * self.specialist_production_yield
        self.gold = self.gold + self.citizen_slot * self.specialist_gold_yield
