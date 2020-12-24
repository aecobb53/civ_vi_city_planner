from backend.common_tile import CommonTile
import math

from backend.district.aqueduct import Aqueduct
from backend.district.dam import Dam
from backend.district.canal import Canal
from backend.improvement.quarry import Quarry
from backend.improvement.mine import Mine
from backend.improvement.lumber_mill import LumberMill

class IndustrialZone(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'workshop',
            'factory',
            'coal_power_plant',
            'oil_power_plant',
            'nuclear_power_plant',
        ]
        self._building_list = None
        self._workshop = None
        self._factory = None
        self._coal_power_plant = None
        self._oil_power_plant = None
        self._nuclear_power_plant = None
        self._powered = None
        self._power = None
        self.specialist_yield = 2
        self.specialist_power_bonus = 1
        self.appeal = self.appeal - 1

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

    # workshop
    @property
    def workshop(self):
        if self._workshop is None:
            return None
        return self._workshop

    @workshop.setter
    def workshop(self, value):
        if value:
            self.production = self.production + 3
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('workshop')
            self._workshop = True

    # factory
    @property
    def factory(self):
        if self._factory is None:
            return None
        return self._factory

    @factory.setter
    def factory(self, value):
        if value:
            self.production = self.production + 3
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('factory')
            self._factory = True
            if self.powered:
                self.production = self.production + 3
                self.citizen_slot = self.citizen_slot + 1

    # coal_power_plant
    @property
    def coal_power_plant(self):
        if self._coal_power_plant is None:
            return None
        return self._coal_power_plant

    @coal_power_plant.setter
    def coal_power_plant(self, value):
        if value:
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_yield += self.specialist_power_bonus
            self.update_building_list('coal_power_plant')
            self._coal_power_plant = True

    @coal_power_plant.deleter
    def coal_power_plant(self):
        if self.coal_power_plant:
            self.citizen_slot = self.citizen_slot - 1
            self.specialist_yield -= self.specialist_power_bonus
            self.update_building_list('coal_power_plant')
            self._coal_power_plant = True

    # oil_power_plant
    @property
    def oil_power_plant(self):
        if self._oil_power_plant is None:
            return None
        return self._oil_power_plant

    @oil_power_plant.setter
    def oil_power_plant(self, value):
        if value:
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_yield += self.specialist_power_bonus
            self.update_building_list('oil_power_plant')
            self._oil_power_plant = True

    @oil_power_plant.deleter
    def oil_power_plant(self):
        if self.oil_power_plant:
            self.citizen_slot = self.citizen_slot - 1
            self.specialist_yield -= self.specialist_power_bonus
            self.update_building_list('oil_power_plant')
            self._oil_power_plant = True

    # nuclear_power_plant
    @property
    def nuclear_power_plant(self):
        if self._nuclear_power_plant is None:
            return None
        return self._nuclear_power_plant

    @nuclear_power_plant.setter
    def nuclear_power_plant(self, value):
        if value:
            self.production = self.production + 4
            self.science = self.science + 3
            self.citizen_slot = self.citizen_slot + 1
            self.specialist_yield += self.specialist_power_bonus
            self.update_building_list('nuclear_power_plant')
            self._nuclear_power_plant = True

    @nuclear_power_plant.deleter
    def nuclear_power_plant(self):
        if self.nuclear_power_plant:
            self.production = self.production - 4
            self.science = self.science - 3
            self.citizen_slot = self.citizen_slot - 1
            self.specialist_yield -= self.specialist_power_bonus
            self.update_building_list('nuclear_power_plant')
            self._nuclear_power_plant = True

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
            final_improvement = 'nuclear_power_plant'
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

        adj_dist_production = 0
        adj_resource = 0
        adj_district = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if adj_obj.district is not None:
                adj_district += 1 # TODO TEST THIS!! HERE
            if isinstance(adj_obj.district, (Aqueduct, Dam, Canal)):
                adj_dist_production += 1
            if isinstance(adj_obj.improvement, Quarry):
                adj_resource += 1
            if adj_obj.resource is not None:
                if adj_obj.resource.resource_type = ='strategic':
                    adj_resource += 1
            if isinstance(adj_obj.improvement, Mine) or isinstance(adj_obj.improvement, LumberMill):
                adj_district += 1
        target_object.production = target_object.production + adj_dist_production * 2
        target_object.production = target_object.production + adj_resource
        target_object.production = target_object.production + math.floor(adj_district / 2)

    def calculate_specialist_yield(self):
        self.production = self.production + self.citizen_slot * self.specialist_yield
