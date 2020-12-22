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
        self._library = None
        self._university = None
        self._research_lab = None
        self._powered = None
        self._power = None
        self.specialist_production_yield = 2
        self.specialist_gold_yield = 2
        self.specialist_power_bonus = 1
        self.appeal = -1

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

    # barracks
    @property
    def barracks(self):
        if self._barracks is None:
            return None
        return self._barracks

    @barracks.setter
    def barracks(self, value):
        if value:
            self.production = self.production + 1
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('barracks')
            self._barracks = True

    @barracks.deleter
    def barracks(self):
        if self._barracks:
            self.production = self.production - 1
            self.houseing = self.houseing - 1
            self.citizen_slot = self.citizen_slot - 1
            self.update_building_list('barracks')
            self._barracks = None
            
    # stable
    @property
    def stable(self):
        if self._stable is None:
            return None
        return self._stable

    @stable.setter
    def stable(self, value):
        if value:
            self.production = self.production + 1
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('stable')
            self._stable = True

    @stable.deleter
    def stable(self):
        if self._stable:
            self.production = self.production - 1
            self.houseing = self.houseing - 1
            self.citizen_slot = self.citizen_slot - 1
            self.remove_building_list('stable')
            self._stable = None
            
    # armory
    @property
    def armory(self):
        if self._armory is None:
            return None
        return self._armory

    @armory.setter
    def armory(self, value):
        if value:
            self.production = self.production + 3
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('armory')
            self._armory = True
            
    # military_academy
    @property
    def military_academy(self):
        if self._military_academy is None:
            return None
        return self._military_academy

    @military_academy.setter
    def military_academy(self, value):
        if value:
            self.production = self.production + 3
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_production_yield += self.specialist_power_bonus
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
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_specialist_yield(self):
        self.production = self.production + self.citizen_slot * self.specialist_production_yield
        self.gold = self.gold + self.citizen_slot * self.specialist_gold_yield
