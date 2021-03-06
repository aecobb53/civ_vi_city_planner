import json
import yaml
import math
import uuid

from backend.common_tile import CommonTile
from backend.tile_container import Tile
from backend.terrain import *
from backend.features import *
from backend.improvements import *
from backend.districts import *
from backend.resources import *

# Config
with open('etc/backend.yml') as ycf:
    config = yaml.load(ycf, Loader=yaml.FullLoader)


class TileManager:
    """
    TileManager manages the tiles. It should be provided with a tile index and a list of tile elements.
    The tile index is the code like cc, i0, o15. the elements are grassland, woods, river.
    Each tile creates a Tile object with the terrain, feature, etc. data stored as objects.
    Each tile object runs off of the common_tile outline.
    """

    def __init__(self, **kwargs):
        """
        The values of the kwargs are converted to lists if they are not already then provided to the Tile class.
        """

        # While i can init the list here like this, i still need to use the getter/setters for every one below... i think
        for tile_index in config['tile_index_list']:
            setattr(self, '_' + tile_index, None)
        self._name = None
        self._erah = None
        self._govener = None
        self._amenities = None
        self._power = None
        self._bonus = None
        self._strategic = None
        self._luxury = None
        self._trader = None
        self._city_uuid = None

        for k, v in kwargs.items():
            if v is None:
                continue
            if not isinstance(v, list):
                v = [v]
            setattr(self, k, v)

        self.adjacency_members = {
            'cc': [self.i0, self.i1, self.i2, self.i3, self.i4, self.i5],
            'i0': [self.m0, self.m1, self.i1, self.cc, self.i5, self.m11],
            'i1': [self.m1, self.m2, self.m3, self.i2, self.cc, self.i0],
            'i2': [self.i1, self.m3, self.m4, self.m5, self.i3, self.cc],
            'i3': [self.cc, self.i2, self.m5, self.m6, self.m7, self.i4],
            'i4': [self.i5, self.cc, self.i3, self.m7, self.m8, self.m9],
            'i5': [self.m11, self.i0, self.cc, self.i4, self.m9, self.m10],
            'm0': [self.o0, self.o1, self.m1, self.i0, self.m11, self.o17],
            'm1': [self.o1, self.o2, self.m2, self.i1, self.i0, self.m0],
            'm2': [self.o2, self.o3, self.o4, self.m3, self.i1, self.m1],
            'm3': [self.m2, self.o4, self.o5, self.m4, self.i2, self.i1],
            'm4': [self.m3, self.o5, self.o6, self.o7, self.m5, self.i2],
            'm5': [self.i2, self.m4, self.o7, self.o8, self.m6, self.i3],
            'm6': [self.i3, self.m5, self.o8, self.o9, self.o10, self.m7],
            'm7': [self.i4, self.i3, self.m6, self.o10, self.o11, self.m8],
            'm8': [self.m9, self.i4, self.m7, self.o11, self.o12, self.o13],
            'm9': [self.m10, self.i5, self.i4, self.m8, self.o13, self.o14],
            'm10': [self.o16, self.m11, self.i5, self.m9, self.o14, self.o15],
            'm11': [self.o17, self.m0, self.i0, self.i5, self.m10, self.o16],
            'o0': [None, None, self.i1, self.m0, self.o17, None],
            'o1': [None, None, self.o2, self.m1, self.m0, self.o0],
            'o2': [None, None, self.o3, self.m2, self.m1, self.o1],
            'o3': [None, None, None, self.o4, self.m2, self.o2],
            'o4': [self.o3, None, None, self.o5, self.m3, self.m2],
            'o5': [self.o4, None, None, self.o6, self.m4, self.m3],
            'o6': [self.o5, None, None, None, self.o7, self.m4],
            'o7': [self.m4, self.o6, None, None, self.o8, self.m5],
            'o8': [self.m5, self.o7, None, None, self.o9, self.m6],
            'o9': [self.m6, self.o8, None, None, None, self.o10],
            'o10': [self.m7, self.m6, self.o9, None, None, self.o11],
            'o11': [self.m8, self.m7, self.o10, None, None, self.o12],
            'o12': [self.o13, self.m8, self.o11, None, None, None],
            'o13': [self.o14, self.m9, self.m8, self.o12, None, None],
            'o14': [self.o15, self.m10, self.m9, self.o13, None, None],
            'o15': [None, self.o16, self.m10, self.o14, None, None],
            'o16': [None, self.o17, self.m11, self.m10, self.o15, None],
            'o17': [None, self.o0, self.m0, self.m11, self.o16, None],
        }

        self.resource_list = config['tile_resources']

        # The order of this one matters I think
        self.tile_list = [
            'wonder',
            'district',
            'terrain',
            'feature',
            'resources',
            'improvement',
        ]

    # cc
    @property
    def cc(self):
        if self._cc is None:
            return None
        return self._cc

    @cc.setter
    def cc(self, value):
        self._cc = Tile(value)

    # i0
    @property
    def i0(self):
        if self._i0 is None:
            return None
        return self._i0

    @i0.setter
    def i0(self, value):
        self._i0 = Tile(value)

    # i1
    @property
    def i1(self):
        if self._i1 is None:
            return None
        return self._i1

    @i1.setter
    def i1(self, value):
        self._i1 = Tile(value)

    # i2
    @property
    def i2(self):
        if self._i2 is None:
            return None
        return self._i2

    @i2.setter
    def i2(self, value):
        self._i2 = Tile(value)

    # i3
    @property
    def i3(self):
        if self._i3 is None:
            return None
        return self._i3

    @i3.setter
    def i3(self, value):
        self._i3 = Tile(value)

    # i4
    @property
    def i4(self):
        if self._i4 is None:
            return None
        return self._i4

    @i4.setter
    def i4(self, value):
        self._i4 = Tile(value)

    # i5
    @property
    def i5(self):
        if self._i5 is None:
            return None
        return self._i5

    @i5.setter
    def i5(self, value):
        self._i5 = Tile(value)

    # m0
    @property
    def m0(self):
        if self._m0 is None:
            return None
        return self._m0

    @m0.setter
    def m0(self, value):
        self._m0 = Tile(value)

    # m1
    @property
    def m1(self):
        if self._m1 is None:
            return None
        return self._m1

    @m1.setter
    def m1(self, value):
        self._m1 = Tile(value)

    # m2
    @property
    def m2(self):
        if self._m2 is None:
            return None
        return self._m2

    @m2.setter
    def m2(self, value):
        self._m2 = Tile(value)

    # m3
    @property
    def m3(self):
        if self._m3 is None:
            return None
        return self._m3

    @m3.setter
    def m3(self, value):
        self._m3 = Tile(value)

    # m4
    @property
    def m4(self):
        if self._m4 is None:
            return None
        return self._m4

    @m4.setter
    def m4(self, value):
        self._m4 = Tile(value)

    # m5
    @property
    def m5(self):
        if self._m5 is None:
            return None
        return self._m5

    @m5.setter
    def m5(self, value):
        self._m5 = Tile(value)

    # m6
    @property
    def m6(self):
        if self._m6 is None:
            return None
        return self._m6

    @m6.setter
    def m6(self, value):
        self._m6 = Tile(value)

    # m7
    @property
    def m7(self):
        if self._m7 is None:
            return None
        return self._m7

    @m7.setter
    def m7(self, value):
        self._m7 = Tile(value)

    # m8
    @property
    def m8(self):
        if self._m8 is None:
            return None
        return self._m8

    @m8.setter
    def m8(self, value):
        self._m8 = Tile(value)

    # m9
    @property
    def m9(self):
        if self._m9 is None:
            return None
        return self._m9

    @m9.setter
    def m9(self, value):
        self._m9 = Tile(value)

    # m10
    @property
    def m10(self):
        if self._m10 is None:
            return None
        return self._m10

    @m10.setter
    def m10(self, value):
        self._m10 = Tile(value)

    # m11
    @property
    def m11(self):
        if self._m11 is None:
            return None
        return self._m11

    @m11.setter
    def m11(self, value):
        self._m11 = Tile(value)

    # o0
    @property
    def o0(self):
        if self._o0 is None:
            return None
        return self._o0

    @o0.setter
    def o0(self, value):
        self._o0 = Tile(value)

    # o1
    @property
    def o1(self):
        if self._o1 is None:
            return None
        return self._o1

    @o1.setter
    def o1(self, value):
        self._o1 = Tile(value)

    # o2
    @property
    def o2(self):
        if self._o2 is None:
            return None
        return self._o2

    @o2.setter
    def o2(self, value):
        self._o2 = Tile(value)

    # o3
    @property
    def o3(self):
        if self._o3 is None:
            return None
        return self._o3

    @o3.setter
    def o3(self, value):
        self._o3 = Tile(value)

    # o4
    @property
    def o4(self):
        if self._o4 is None:
            return None
        return self._o4

    @o4.setter
    def o4(self, value):
        self._o4 = Tile(value)

    # o5
    @property
    def o5(self):
        if self._o5 is None:
            return None
        return self._o5

    @o5.setter
    def o5(self, value):
        self._o5 = Tile(value)

    # o6
    @property
    def o6(self):
        if self._o6 is None:
            return None
        return self._o6

    @o6.setter
    def o6(self, value):
        self._o6 = Tile(value)

    # o7
    @property
    def o7(self):
        if self._o7 is None:
            return None
        return self._o7

    @o7.setter
    def o7(self, value):
        self._o7 = Tile(value)

    # o8
    @property
    def o8(self):
        if self._o8 is None:
            return None
        return self._o8

    @o8.setter
    def o8(self, value):
        self._o8 = Tile(value)

    # o9
    @property
    def o9(self):
        if self._o9 is None:
            return None
        return self._o9

    @o9.setter
    def o9(self, value):
        self._o9 = Tile(value)

    # o10
    @property
    def o10(self):
        if self._o10 is None:
            return None
        return self._o10

    @o10.setter
    def o10(self, value):
        self._o10 = Tile(value)

    # o11
    @property
    def o11(self):
        if self._o11 is None:
            return None
        return self._o11

    @o11.setter
    def o11(self, value):
        self._o11 = Tile(value)

    # o12
    @property
    def o12(self):
        if self._o12 is None:
            return None
        return self._o12

    @o12.setter
    def o12(self, value):
        self._o12 = Tile(value)

    # o13
    @property
    def o13(self):
        if self._o13 is None:
            return None
        return self._o13

    @o13.setter
    def o13(self, value):
        self._o13 = Tile(value)

    # o14
    @property
    def o14(self):
        if self._o14 is None:
            return None
        return self._o14

    @o14.setter
    def o14(self, value):
        self._o14 = Tile(value)

    # o15
    @property
    def o15(self):
        if self._o15 is None:
            return None
        return self._o15

    @o15.setter
    def o15(self, value):
        self._o15 = Tile(value)

    # o16
    @property
    def o16(self):
        if self._o16 is None:
            return None
        return self._o16

    @o16.setter
    def o16(self, value):
        self._o16 = Tile(value)

    # o17
    @property
    def o17(self):
        if self._o17 is None:
            return None
        return self._o17

    @o17.setter
    def o17(self, value):
        self._o17 = Tile(value)

    # name
    @property
    def name(self):
        if self._name is None:
            return None
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, list):
            value = [value]
        self._name = value[0]

    # erah
    @property
    def erah(self):
        if self._erah is None:
            return 8
        return self._erah

    @erah.setter
    def erah(self, value):
        if not isinstance(value, list):
            value = [value]
        self._erah = value[0]

    # govener
    @property
    def govener(self):
        if self._govener is None:
            return None
        return self._govener

    @govener.setter
    def govener(self, value):
        self._govener = Tile(value)

    # amenities
    @property
    def amenities(self):
        if self._amenities is None:
            return None
        return self._amenities

    @amenities.setter
    def amenities(self, value):
        self._amenities = Tile(value)

    # power
    @property
    def power(self):
        if self._power is None:
            return None
        return self._power

    @power.setter
    def power(self, value):
        self._power = Tile(value)

    # bonus
    @property
    def bonus(self):
        if self._bonus is None:
            return None
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        self._bonus = Tile(value)

    # strategic
    @property
    def strategic(self):
        if self._strategic is None:
            return None
        return self._strategic

    @strategic.setter
    def strategic(self, value):
        self._strategic = Tile(value)

    # luxury
    @property
    def luxury(self):
        if self._luxury is None:
            return None
        return self._luxury

    @luxury.setter
    def luxury(self, value):
        self._luxury = Tile(value)

    # trader
    @property
    def trader(self):
        if self._trader is None:
            return None
        return self._trader

    @trader.setter
    def trader(self, value):
        self._trader = Tile(value)

    # city_uuid
    @property
    def city_uuid(self):
        if self._city_uuid is None:
            self.city_uuid = self._generate_uuid()
        return self._city_uuid

    @city_uuid.setter
    def city_uuid(self, value):
        if self._city_uuid is None:
            self._city_uuid = value

    def _generate_uuid(self):
        return uuid.uuid1().hex

    def _tile_summer(self, tile_index, tile_type, resource):
        # print(self, tile_index, tile_type, resource)
        # print(getattr(getattr(getattr(self, tile_index), tile_type), resource))
        try:
            orig_yield = getattr(getattr(self, tile_index), resource)
            tile_yield = getattr(getattr(getattr(self, tile_index), tile_type), resource)
            new_yield = orig_yield + tile_yield
            setattr(getattr(self, tile_index), resource, new_yield)
            return tile_yield
            # return getattr(getattr(getattr(self, tile_index), tile_type), resource)
        except AttributeError:
            return None
        except TypeError:
            pass

    def _calculate_district(self, tile_index):
        # Calculate the yield and details around the district
        # print(getattr(self, tile_index).district)
        for resource in self.resource_list:
            # print(f"----resource: {resource}")
            self._tile_summer(tile_index, 'district', resource)

        try:
            getattr(self, tile_index).district.calculate_adjacency(self, tile_index, self.adjacency_members[tile_index])
        except AttributeError:
            pass

    def _calculate_terrain(self, tile_index):
        # Calculate the yield for the terrain of the tile
        for resource in self.resource_list:
            self._tile_summer(tile_index, 'terrain', resource)

    def _calculate_hills(self, tile_index):
        # Calculate the yield for the hills of the tile
        for resource in self.resource_list:
            self._tile_summer(tile_index, 'hills', resource)

    def _calculate_feature(self, tile_index):
        # Calculate the yield for the feature of the tile
        for resource in self.resource_list:
            self._tile_summer(tile_index, 'feature', resource)

    def _calculate_resource(self, tile_index):
        # Calculate the yield for the improvement on the tile
        for resource in self.resource_list:
            self._tile_summer(tile_index, 'resource', resource)

    def _calculate_improvement(self, tile_index):
        # Calculate the yield for the improvement on the tile
        for resource in self.resource_list:
            self._tile_summer(tile_index, 'improvement', resource)

        try:
            getattr(self, tile_index).improvement.calculate_adjacency(self, tile_index, self.adjacency_members[tile_index])
        except AttributeError:
            pass

        try:
            getattr(self, tile_index).improvement.calculate_erah(self, tile_index, self.adjacency_members[tile_index])
        except AttributeError:
            pass

    # def set_attribute(attribute, value):
    #     setattr(self, attribute, value)

    # def append_attribute(attribute, value):
    #     if 
    #     getattr(self, attribute).append(value)

    def calculate_tile_yield(self, tile_index):
        """
        This will run both the adjacency and era calculators to get a final tile yield.
        """
        # if tile_index is None:
        #     print('for testing only running first few keys. Fix this later!!!!')
        #     search_list = list(self.adjacency_members.keys())[:7]
        #     # search_list = self.adjacency_members.keys()
        # else:
        #     if not isinstance(tile_index, list):
        #         search_list = [tile_index]

        if getattr(self, tile_index) is None:
            return None

        if getattr(self, tile_index).wonder is not None:
            print('has wonder')
            # self._calculate_wonder(tile_index)
            return None

        if getattr(self, tile_index).district is not None:
            print('has district')
            self._calculate_district(tile_index)
            return None

        if getattr(self, tile_index).terrain is not None:
            print('has terrain')
            self._calculate_terrain(tile_index)

        if getattr(self, tile_index).hills is not None:
            print('has hills')
            self._calculate_hills(tile_index)

        if getattr(self, tile_index).feature is not None:
            print('has feature')
            self._calculate_feature(tile_index)

        # if getattr(self, tile_index).river is not None:
        #     print('has river')
        #     # self._calculate_river(tile_index)

        if getattr(self, tile_index).resource is not None:
            self._calculate_resource(tile_index)
            print('has resource')

        if getattr(self, tile_index).improvement is not None:
            print('has improvement')
            self._calculate_improvement(tile_index)

    def sum_city_tiles(self):
        for metric in config['city_metrics']:
            for tile_index in list(self.adjacency_members.keys()):
                try:
                    print(f"sum tile stuff: {metric}, {tile_index}, {getattr(getattr(self, tile_index), metric)}")
                    tile_value = getattr(getattr(self, tile_index), metric)
                except AttributeError:
                    continue
                try:
                    if metric == 'erah':
                        self.erah = max(self.erah, tile_value)
                    elif metric == 'city_uuid':
                        continue
                    else:
                        if tile_value is None:
                            continue
                        try:
                            new_value = getattr(self, metric) + tile_value
                        except AttributeError:
                            new_value = tile_value
                        setattr(self, metric, new_value)
                except TypeError:
                    pass
                

    def calculate_city_yield(self):
        # print('for testing only running first few keys. Fix this later!!!!')
        # search_list = list(self.adjacency_members.keys())[:7]
        search_list = list(self.adjacency_members.keys())
        for tile_index in search_list:
            self.calculate_tile_yield(tile_index)
        self.sum_city_tiles()

    def return_adj_matrix(self, tile_index):
        """
        This keeps track of the tile's adjacency list. The list is either the object or None if there is not one.
        This may need to be updated eventually in case I keep track of surrounding tiles outside of the city that still influence it.
        """
        return self.adjacency_members[tile_index]

    def converte_to_json(self):
        return_dict = {}
        for tile_index in config['tile_index_list']:
            temp_container = {}
            tile = getattr(self, tile_index)
            if tile is None:
                continue
            for layer in config['tile_layers']:
                if getattr(tile, layer) is not None:
                    temp_container[layer] = str(getattr(tile, layer)).split('.')[2]
            if temp_container != {}:
                return_dict[tile_index] = temp_container
        if self.name is not None:
            return_dict['name'] = self.name

        if self.erah is not None:
            return_dict['erah'] = self.erah

        if self.govener is not None:
            return_dict['govener'] = self.govener

        if self.amenities is not None:
            return_dict['amenities'] = self.amenities

        if self.power is not None:
            return_dict['power'] = self.power

        if self.bonus is not None:
            return_dict['bonus'] = self.bonus

        if self.strategic is not None:
            return_dict['strategic'] = self.strategic

        if self.luxury is not None:
            return_dict['luxury'] = self.luxury

        if self.trader is not None:
            return_dict['trader'] = self.trader

        if self.city_uuid is not None:
            return_dict['city_uuid'] = self.city_uuid

        self.calculate_city_yield()
        for metric in config['city_metrics']:
            if getattr(self, metric) is not None:
                return_dict[metric] = getattr(self, metric)

        return return_dict

    # def json_to_object(self, city_json):
    #     for k, v in city_json.items():
    #         if k not in config['tile_index_list']:
    #             continue
    #         print(k,v)
    #     # uuid.UUID(hex=('hex value here'))
    #     return self
