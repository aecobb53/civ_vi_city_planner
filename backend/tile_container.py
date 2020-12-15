from common_tile import CommonTile
from terrain.grassland import Grassland
from terrain.plains import Plains
from features.woods import Woods
from features.floodplains import Floodplains
from improvements.farm import Farm
from districts.campus import Campus

class Tile(CommonTile):
    """
    This manages the aspects of a tile. Simple things like ther can only be one terrain feature. 
    """

    def __init__(
        self, 
        tile_list):
        super().__init__()
        self._terrain = None
        self._feature = None
        self._river = None
        self._improvement = None
        self._district = None
        self._wonder = None

        self.list_of_terrain = [
            'grassland',
            'grasslandh',
            'plains',
            'plainsh',
            'desert',
            'deserth',
            'tundra',
            'tundrah',
            'snow',
            'snowh',
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
        self.list_of_improvements = [
            'farm',
        ]
        self.list_of_districts = [
            'campus'
        ]
        self.list_of_wonders = []

        for name in tile_list:
            # print(type(name))
            # print(name)

            if name in self.list_of_terrain:
                # print('type is terrain')
                print(name)
                if name.endswith('h'):
                    hills = True
                else:
                    hills = False
                if 'grassland' in name:
                    # print('type is grassland')
                    self.terrain = Grassland(hills=hills)

            if name in self.list_of_features:
                # print('type is feature')
                if name == 'woods':
                    # print('type is woods')
                    self.feature = Woods()
                if name == 'floodplains':
                    self.feature = Floodplains()

            if name == 'river':
                # print('type has a river')
                self.river = True

            if name in self.list_of_improvements:
                print('type is improvement')
                if name == 'farm':
                    print('type is farm')
                    self.improvement = Farm()
                    print(self.improvement.__dict__)
            
            if name in self.list_of_districts:
                print('type is district')
                if name == 'campus':
                    print('type is campus')
                    self.district = Campus()
                    self.district.set_buildings()

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

    # river
    @property
    def river(self):
        if self._river == None:
            return None
        return self._river

    @river.setter
    def river(self, value):
        self._river = value

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

    # def return_yield(self):


