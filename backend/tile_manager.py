import json
import math

from common_tile import CommonTile
from tile_container import Tile
from terrain.grassland import Grassland
from terrain.plains import Plains
from features.woods import Woods
from improvements.farm import Farm


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
        
        self.cc = None
        self.i0 = None
        self.i1 = None
        self.i2 = None
        self.i3 = None
        self.i4 = None
        self.i5 = None
        self.m0 = None
        self.m1 = None
        self.m2 = None
        self.m3 = None
        self.m4 = None
        self.m5 = None
        self.m6 = None
        self.m7 = None
        self.m8 = None
        self.m9 = None
        self.m10 = None
        self.m11 = None
        self.o0 = None
        self.o1 = None
        self.o2 = None
        self.o3 = None
        self.o4 = None
        self.o5 = None
        self.o6 = None
        self.o7 = None
        self.o8 = None
        self.o9 = None
        self.o10 = None
        self.o11 = None
        self.o12 = None
        self.o13 = None
        self.o14 = None
        self.o15 = None
        self.o16 = None
        self.o17 = None

        self.erah = None
        self.govener = None
        self.amenities = None
        self.power = None
        self.bonus = None
        self.strategic = None
        self.luxury = None
        self.trader = None

        for k,v in kwargs.items():
            if not isinstance(v, list):
                v = [v]
            if k == 'cc':
                self.cc = Tile(v)
            if k == 'i0':
                self.i0 = Tile(v)
            if k == 'i1':
                self.i1 = Tile(v)
            if k == 'i2':
                self.i2 = Tile(v)
            if k == 'i3':
                self.i3 = Tile(v)
            if k == 'i4':
                self.i4 = Tile(v)
            if k == 'i5':
                self.i5 = Tile(v)
            if k == 'm0':
                self.m0 = Tile(v)
            if k == 'm1':
                self.m1 = Tile(v)
            if k == 'm2':
                self.m2 = Tile(v)
            if k == 'm3':
                self.m3 = Tile(v)
            if k == 'm4':
                self.m4 = Tile(v)
            if k == 'm5':
                self.m5 = Tile(v)
            if k == 'm6':
                self.m6 = Tile(v)
            if k == 'm7':
                self.m7 = Tile(v)
            if k == 'm8':
                self.m8 = Tile(v)
            if k == 'm9':
                self.m9 = Tile(v)
            if k == 'm10':
                self.m10 = Tile(v)
            if k == 'm11':
                self.m11 = Tile(v)
            if k == 'o0':
                self.o0 = Tile(v)
            if k == 'o1':
                self.o1 = Tile(v)
            if k == 'o2':
                self.o2 = Tile(v)
            if k == 'o3':
                self.o3 = Tile(v)
            if k == 'o4':
                self.o4 = Tile(v)
            if k == 'o5':
                self.o5 = Tile(v)
            if k == 'o6':
                self.o6 = Tile(v)
            if k == 'o7':
                self.o7 = Tile(v)
            if k == 'o8':
                self.o8 = Tile(v)
            if k == 'o9':
                self.o9 = Tile(v)
            if k == 'o10':
                self.o10 = Tile(v)
            if k == 'o11':
                self.o11 = Tile(v)
            if k == 'o12':
                self.o12 = Tile(v)
            if k == 'o13':
                self.o13 = Tile(v)
            if k == 'o14':
                self.o14 = Tile(v)
            if k == 'o15':
                self.o15 = Tile(v)
            if k == 'o16':
                self.o16 = Tile(v)
            if k == 'o17':
                self.o17 = Tile(v)

            if k == 'erah':
                self.erah = v[0]
            if k == 'govener':
                self.govener = v
            if k == 'amenities':
                self.amenities = v
            if k == 'power':
                self.power = v
            if k == 'bonus':
                self.bonus = v
            if k == 'strategic':
                self.strategic = v
            if k == 'luxury':
                self.luxury = v
            if k == 'trader':
                self.trader = v

        # Era:0 Ancient Era (4000 BC ~ 1000 BC)
        # Era:1 Classical Era (1000 BC ~ 500 AD)
        # Era:2 Medieval Era (500 ~ 1350)
        # Era:3 Renaissance Era (1350 ~ 1725)
        # Era:4 Industrial Era (1725 ~ 1890)
        # Era:5 Modern Era (1890 ~ 1945)
        # Era:6 Atomic Era (1945 ~ 1995)
        # Era:7 Information Era (1995 ~ 2020)
        # Era:8 Future Era GS-Only.png (2020 ~ 2050)
        # print(json.dumps(self.__dict__, indent=4))
        print(f"cc: {self.cc}")
        print(f"i0: {self.i0}")
        print(f"i1: {self.i1}")
        print(f"i2: {self.i2}")
        print(f"i3: {self.i3}")
        print(f"i4: {self.i4}")
        print(f"i5: {self.i5}")
        print(f"m0: {self.m0}")
        print(f"m1: {self.m1}")
        print(f"m2: {self.m2}")
        print(f"m3: {self.m3}")
        print(f"m4: {self.m4}")
        print(f"m5: {self.m5}")
        print(f"m6: {self.m6}")
        print(f"m7: {self.m7}")
        print(f"m8: {self.m8}")
        print(f"m9: {self.m9}")
        print(f"m10: {self.m10}")
        print(f"m11: {self.m11}")
        print(f"o0: {self.o0}")
        print(f"o1: {self.o1}")
        print(f"o2: {self.o2}")
        print(f"o3: {self.o3}")
        print(f"o4: {self.o4}")
        print(f"o5: {self.o5}")
        print(f"o6: {self.o6}")
        print(f"o7: {self.o7}")
        print(f"o8: {self.o8}")
        print(f"o9: {self.o9}")
        print(f"o10: {self.o10}")
        print(f"o11: {self.o11}")
        print(f"o12: {self.o12}")
        print(f"o13: {self.o13}")
        print(f"o14: {self.o14}")
        print(f"o15: {self.o15}")
        print(f"o16: {self.o16}")
        print(f"o17: {self.o17}")

    def calculate_adjacency(self, tile_index):
        """
        Many tile elements are dependant on the surrounding tiles. This will go through each adjacent tile
        and apply the appropriate adjacency bonuses if there are any. 
        """
        # print(tile_index)
        adj_farm_count = 0
        for dex in self.return_adj_matrix(tile_index):
            try:
                # print('    ' + str(dex) + '  -  ' + str(dex.terrain) + '  =  ' + str(dex.improvement))
                if isinstance(dex.improvement, Farm):
                    adj_farm_count +=1
            except:
                pass
        if isinstance(getattr(self, tile_index).improvement, Farm):
            print(f"The number of 2 adj farms is {math.floor(adj_farm_count / 2)}")

    def calculate_era(self, tile_index):
        """
        Many tile elements benefit from technologies in the different eras. 
        It would be nice to be able to input that and not just the endgame era. 
        """
        pass

    def calculate_tile_yield(self, tile_index):
        """
        This will run both the adjacency and era calculators to get a final tile yield. 
        """
        pass

    def return_adj_matrix(self, tile_index):
        """
        This keeps track of the tile's adjacency list. The list is either the object or None if there is not one. 
        This may need to be updated eventually in case I keep track of surrounding tiles outside of the city that still influence it. 
        """
        adjacency_members = {
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
        return adjacency_members[tile_index]

        













tm = TileManager(

        erah=1,

        cc=[
            'grassland',
            'woods',
            'river',
            'farm',
        ],

        i0=[
            'grassland',
            'woods',
            'river',
            'farm',
        ],

        i1=[
            'grassland',
            'woods',
            'river',
            'farm',
        ],

        i2=[
            'grassland',
            'woods',
            'river',
            'farm',
        ],

        i3=[
            'grassland',
            'woods',
            'river',
        ],

        i4=[
            'grassland',
            'woods',
            'river',
        ],

        i5=[
            'grassland',
            'woods',
            'river',
        ],
)
gl = Grassland()
wd = Woods()

# print(tm.__dict__)
# print(tm.i0.__dict__)
# print(tm.i0.terrain.__dict__)
# print('')
print(tm.calculate_adjacency('i0'))
# print(tm.calculate_adjacency('cc'))
# print(tm._cc.__dict__)
# print(json.dumps(tm.__dict__, indent=2))

# print(json.dumps(gl.__dict__, indent=4))
# print(gl.food)
# gl.food = 1
# print(gl.food)