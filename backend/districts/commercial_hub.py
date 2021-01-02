from backend.common_tile import CommonTile
import math

from backend.districts.harbor import Harbor
from backend.features.river import River


class CommercialHub(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'market',
            'bank',
            'stock_exchange',
        ]
        self._building_list = None
        self._market = None
        self._bank = None
        self._stock_exchange = None
        self._powered = None
        self._power = None
        self.specialist_yield = 4
        self.specialist_power_bonus = 2

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

    # market
    @property
    def market(self):
        if self._market is None:
            return False
        return self._market

    @market.setter
    def market(self, value):
        if value:
            self.gold = self.gold + 3
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('market')
            self._market = True

    # bank
    @property
    def bank(self):
        if self._bank is None:
            return False
        return self._bank

    @bank.setter
    def bank(self, value):
        if value:
            self.gold = self.gold + 5
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('bank')
            self._bank = True

    # stock_exchange
    @property
    def stock_exchange(self):
        if self._stock_exchange is None:
            return False
        return self._stock_exchange

    @stock_exchange.setter
    def stock_exchange(self, value):
        if value:
            self.gold = self.gold + 4
            self.citizen_slot = self.citizen_slot + 1
            if self.powered:
                self.gold = self.gold + 7
                self.specialist_yield += self.specialist_power_bonus
            self.update_building_list('stock_exchange')
            self._stock_exchange = True

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
            self.powered = True

        for building in self.default_building_list:
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)

    def calculate_adjacency(self, tile_obj, target_index, adj_list):  # pragma: no cover
        target_object = getattr(tile_obj, target_index)

        adj_harbor = 0
        adj_districts = 0
        for adj_obj in adj_list:
            if adj_obj is None:
                continue
            if adj_obj.district is not None:
                adj_district += 1  # TODO TEST THIS!! HERE
            if isinstance(adj_obj.feature, Harbor):
                adj_harbor += 1
            if isinstance(adj_obj.feature, River):
                adj_harbor += 1
        target_object.gold = target_object.gold + (adj_harbor * 2)
        target_object.gold = target_object.gold + math.floor(adj_district / 2)

    def calculate_specialist_yield(self):
        self.gold = self.gold + self.citizen_slot * self.specialist_yield
