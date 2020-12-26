from backend.common_tile import CommonTile
import math

# from backend.districts.water_park import WaterPark
# from backend.districts.entertainment_complex import EntertainmentComplex

class Neighborhood(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'food_market',
            'shopping_mall',
        ]
        self._building_list = None
        self._food_market = None
        self._shopping_mall = None
        self._powered = None
        self._power = None

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
        if self._building_list == None:
            return None
        self._building_list.remove(value)

    # food_market
    @property
    def food_market(self):
        if self._food_market is None:
            return False
        return self._food_market

    @food_market.setter
    def food_market(self, value):
        if value:
            self.food = self.food + 4
            self.maintenance = self.maintenance + 1
            if self.powered:
                self.food = self.food + 2
            if self.shopping_mall:
                del self.shopping_mall
            self.update_building_list('food_market')
            self._food_market = True

    @food_market.deleter
    def food_market(self):
        if self.food_market:
            self.food = self.food - 4
            self.maintenance = self.maintenance - 1
            if self.powered:
                self.food = self.food - 2
            self.remove_building_list('food_market')
            self._food_market = None

    # shopping_mall
    @property
    def shopping_mall(self):
        if self._shopping_mall is None:
            return False
        return self._shopping_mall

    @shopping_mall.setter
    def shopping_mall(self, value):
        if value:
            self.gold = self.gold + 2
            self.amenities = self.amenities + 1
            self.maintenance = self.maintenance + 1
            if self.powered:
                self.gold = self.gold + 2
                self.amenities = self.amenities + 1
            if self.food_market:
                del self.food_market
            self.update_building_list('shopping_mall')
            self._shopping_mall = True

    @shopping_mall.deleter
    def shopping_mall(self):
        if self.shopping_mall:
            self.gold = self.gold - 2
            self.amenities = self.amenities - 1
            self.maintenance = self.maintenance - 1
            if self.powered:
                self.gold = self.gold - 2
                self.amenities = self.amenities - 1
            self.remove_building_list('shopping_mall')
            self._shopping_mall = None

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
        self.power = 1
        self._powered = value

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement == None:
            self.powered = True
            final_improvement = 'shopping_mall'
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

        target_object.houseing = target_object.houseing
        if target_object.appeal >= 4:
            target_object += 6
        if target_object.appeal >= 2 and target_object.appeal < 4:
            target_object += 5
        if target_object.appeal >= -1 and target_object.appeal < 2:
            target_object += 4
        if target_object.appeal >= -3 and target_object.appeal < -1:
            target_object += 3
        if target_object.appeal <= -4:
            target_object += 2

    def calculate_specialist_yield(self):
        # self.culture = self.culture + self.citizen_slot * self.specialist_yield
        pass
