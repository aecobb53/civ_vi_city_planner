from common_tile import CommonTile
from terrain.grassland import Grassland
from terrain.plains import Plains
from features.woods import Woods
from features.floodplains import Floodplains
from improvements.farm import Farm
from districts.campus import Campus
from resources.bananas import Bananas
from improvements.plantation import Plantation

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
        self._resource = None
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
            'mine',
            'quarry',
            'plantation',
            'camp',
            'pasture',
            'fishing_boat',
            'lumber_mill',
            'fort',
            'airstrip',
            'seaside_resprot',
            'geothermal_plant',
            'wind_farm',
            'solar_farm',
            'offshore_wind_farm',
            'ski_resort',
            'oil_well',
            'offshore_oil_well',
            'missle_silo',
            'mountain_tunnel',
            'railroad',
            'seastead',
            'alcazar',
            'batey',
            'cahokia_mounds',
            'colossal_heads',
            'mahavihara',
            'moai',
            'monistary',
            'nazca_line',
            'trading_dome',
            'chateau',
            'chemamull',
            'golf_course',
            'great_wall',
            'hacienda',
            'ice_hocky_rink',
            'kampung',
            'kurgan',
            'mekewap',
            'mission',
            'nubian_pyramid',
            'open-air_museum',
            'outback_station',
            'pa',
            'pairirdaeza',
            'polder',
            'qhapaq_nan',
            'rock-hewn_church',
            'roman_fort',
            'sphinx',
            'stepwell',
            'terrace_farms',
            'ziggurat',
            'city_park',
            'fishery',
        ]
        self.list_of_districts = [
            'city_center',
            'campus',
            'theater_square',
            'holy_site',
            'encampment',
            'commercial_hub',
            'harbor',
            'industrial_zone',
            'entertainment_complex',
            'water_park',
            'aqueduct',
            'neighborhood',
            'canal',
            'dam',
            'aerodrome',
            'spaceport',
            'govermment_plaza',
            'diplomatic_quarter',
        ]
        self.list_of_resources = [
            'bananas',
            'copper',
            'cattle',
            'crabs',
            'deer',
            'fish',
            'maize',
            'rice',
            'sheep',
            'stone',
            'wheat',
            'amber',
            'cinnamon',
            'citrus',
            'cloves',
            'cocoa',
            'coffee',
            'cosmetics',
            'cotton',
            'dyes',
            'diamonds',
            'furs',
            'gold_ore',
            'gypsum',
            'honey',
            'insense',
            'ivory',
            'jade',
            'jeans',
            'marble',
            'murcury',
            'olives',
            'pearls',
            'perfume',
            'salt',
            'silk',
            'silver',
            'spices',
            'sugar',
            'tea',
            'tobacco',
            'toys',
            'truffles',
            'turtles',
            'whales',
            'wine',
            'horses',
            'iron',
            'niter',
            'coal',
            'oil',
            'aluminum',
            'uranium',
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
                if name == 'plantation':
                    print('type is plantation')
                    self.improvement = Plantation()
            
            if name in self.list_of_districts:
                print('type is district')
                if name == 'campus':
                    print('type is campus')
                    self.district = Campus()
                    self.district.set_buildings()

            if name in self.list_of_resources:
                print('type is resource')
                if name == 'bananas':
                    print('type is bananas')
                    self.resource = Bananas()




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

    # resource
    @property
    def resource(self):
        if self._resource == None:
            return None
        return self._resource

    @resource.setter
    def resource(self, value):
        self._resource = value

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


