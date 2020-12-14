import json

from common_tile import CommonTile
from terrain.grassland import Grassland
from features.woods import Woods

class TileManager:

    def __init__(self, **kwargs):
        self._cc = None
        self._i0 = None
        for k,v in kwargs.items():
            if not isinstance(v, list):
                v = [v]
            if k == 'cc':
                self.cc = Tile(v)
            if k == 'i0':
                self.i0 = Tile(v)
        

class Tile:

    def __init__(self, tile_list):
        self._terrain = None
        self._feature = None
        self._improvement = None
        self._district = None
        self._wonder = None

        self.list_of_terrain = [
            'grassland',
            'plains',
            'desert',
            'tundra',
            'snow',
            'coast',
            'lake',
            'ocean',
        ]
        self.list_of_features = [
            'woods',
            'rainforest',
            'marsh',
            'floodplains',
            'oasis',
            'mountains',
            'cliffs',
            'reef',
            'ice',
            'cataract',
            'volcano',
            'volcanic_soil',
            'geothermal',
        ]
        self.list_of_improvements = []
        self.list_of_districts = []
        self.list_of_wonders = []

        for name in tile_list:
            print(type(name))
            print(name)

            if name in self.list_of_terrain:
                print('type is terrain')
                if name == 'grassland':
                    print('type is grassland')
                    self.terrain = Grassland()

            if name in self.list_of_features:
                print('type is terrain')
                if name == 'woods':
                    print('type is woods')
                    self.feature = Woods()

    # terrain
    @property
    def terrain(self):
        if self._terrain == None:
            return None
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        self._terrain = value

    # feature
    @property
    def feature(self):
        if self._feature == None:
            return None
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value

    # improvement
    @property
    def improvement(self):
        if self._improvement == None:
            return None
        return self._improvement

    @improvement.setter
    def improvement(self, value):
        self._improvement = value

    # district
    @property
    def district(self):
        if self._district == None:
            return None
        return self._district

    @district.setter
    def district(self, value):
        self._district = value

    # wonder
    @property
    def wonder(self):
        if self._wonder == None:
            return None
        return self._wonder

    @wonder.setter
    def wonder(self, value):
        self._wonder = value













tm = TileManager(
    cc='grassland',
    i0=[
        'grassland',
        'woods'])
gl = Grassland()
wd = Woods()

print(tm.__dict__)
print(tm.i0.__dict__)
print(tm.i0.terrain.__dict__)
# print(tm._cc.__dict__)
# print(json.dumps(tm.__dict__, indent=2))

# print(json.dumps(gl.__dict__, indent=4))
# print(gl.food)
# gl.food = 1
# print(gl.food)