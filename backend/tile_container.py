# from common_tile import CommonTile
# from terrain.grassland import Grassland
# from terrain.plains import Plains
# from features.woods import Woods
# from features.floodplains import Floodplains
# from improvements.farm import Farm
# from districts.campus import Campus
# from resources.bananas import Bananas
# from improvements.plantation import Plantation

from common_tile import CommonTile
from terrain import *
from features import *
from improvements import *
from districts import *
from resources import *


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
            'mountain',
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
            'fishing_boats',
            'lumber_mill',
            'fort',
            'airstrip',
            'seaside_resort',
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
            'open_air_museum',
            'outback_station',
            'pa',
            'pairirdaeza',
            'polder',
            'qhapaq_nan',
            'rock_hewn_church',
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

        tile_parts = {
            'terrain': None,
            'features': None,
            'river': None,
            'resources': None,
            'improvements': None,
            'districts': None,
        }

        for name in tile_list:
            # First i need to make sure the order of everything is correct
            if ':' in name:
                """
                If i want specific buildings in a district i append the district with a :building name or :building_number
                ex: campus
                ex: campus:2
                ex: campus:univeristy
                """
                dist_name = name.split(':')
            else:
                dist_name = [name]

            if name in self.list_of_terrain:
                tile_parts['terrain'] = name

            if name in self.list_of_features:
                tile_parts['features'] = name

            if name == 'river':
                tile_parts['river'] = name

            if name in self.list_of_improvements:
                tile_parts['improvements'] = name

            if dist_name[0] in self.list_of_districts:
                tile_parts['districts'] = name

            if name in self.list_of_resources:
                tile_parts['resources'] = name


        for name in tile_parts.values():
            # Then i loop through the dict that was just created to assign things in order
            if name is None:
                continue
            if ':' in name:
                """
                If i want specific buildings in a district i append the district with a :building name or :building_number
                ex: campus
                ex: campus:2
                ex: campus:univeristy
                """
                dist_name = name.split(':')
            else:
                dist_name = [name]

            if name in self.list_of_terrain:
                # print('type is terrain')
                # print(name)
                if name.endswith('h'):
                    hills = True
                else:
                    hills = False

                if 'grassland' in name:
                    self.terrain = Grassland(hills=hills)

                if 'plains' in name:
                    self.terrain = Plains(hills=hills)

                if 'desert' in name:
                    self.terrain = Desert(hills=hills)

                if 'tundra' in name:
                    self.terrain = Tundra(hills=hills)

                if 'snow' in name:
                    self.terrain = Snow(hills=hills)

                if 'coast' in name:
                    self.terrain = Coast(hills=hills)

                if 'lake' in name:
                    self.terrain = Lake(hills=hills)

                if 'ocean' in name:
                    self.terrain = Ocean(hills=hills)


            if name in self.list_of_features:
                if 'woods' in name:
                    self.feature = Woods()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'rainforest' in name:
                    self.feature = Rainforest()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'marsh' in name:
                    self.feature = Marsh()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'floodplains' in name:
                    self.feature = Floodplains()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'oasis' in name:
                    self.feature = Oasis()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'mountain' in name:
                    self.feature = Mountain()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'cliffs' in name:
                    self.feature = Cliffs()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'reef' in name:
                    self.feature = Reef()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'ice' in name:
                    self.feature = Ice()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'cataract' in name:
                    self.feature = Cataract()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'volcano' in name:
                    self.feature = Volcano()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'volcanic_soil' in name:
                    self.feature = Volcanic_soil()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

                if 'geothermal' in name:
                    self.feature = Geothermal()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    if terrain_type not in self.feature.acceptable_terrain:
                        self.feature = None

            if name == 'river':
                # print('type has a river')
                self.river = True

            if name in self.list_of_resources:
                # print('type is resource')

                if name == 'bananas':
                    self.resource = Bananas()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'copper':
                    self.resource = Copper()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cattle':
                    self.resource = Cattle()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'crabs':
                    self.resource = Crabs()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'deer':
                    self.resource = Deer()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'fish':
                    self.resource = Fish()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'maize':
                    self.resource = Maize()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'rice':
                    self.resource = Rice()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'sheep':
                    self.resource = Sheep()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'stone':
                    self.resource = Stone()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'wheat':
                    self.resource = Wheat()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'amber':
                    self.resource = Amber()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cinnamon':
                    self.resource = Cinnamon()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'citrus':
                    self.resource = Citrus()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cloves':
                    self.resource = Cloves()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cocoa':
                    self.resource = Cocoa()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'coffee':
                    self.resource = Coffee()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cosmetics':
                    self.resource = Cosmetics()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'cotton':
                    self.resource = Cotton()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'dyes':
                    self.resource = Dyes()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'diamonds':
                    self.resource = Diamonds()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'furs':
                    self.resource = Furs()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'gold_ore':
                    self.resource = Gold_ore()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'gypsum':
                    self.resource = Gypsum()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'honey':
                    self.resource = Honey()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'insense':
                    self.resource = Insense()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'ivory':
                    self.resource = Ivory()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'jade':
                    self.resource = Jade()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'jeans':
                    self.resource = Jeans()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'marble':
                    self.resource = Marble()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'murcury':
                    self.resource = Murcury()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'olives':
                    self.resource = Olives()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'pearls':
                    self.resource = Pearls()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'perfume':
                    self.resource = Perfume()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'salt':
                    self.resource = Salt()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'silk':
                    self.resource = Silk()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'silver':
                    self.resource = Silver()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'spices':
                    self.resource = Spices()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'sugar':
                    self.resource = Sugar()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'tea':
                    self.resource = Tea()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'tobacco':
                    self.resource = Tobacco()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'toys':
                    self.resource = Toys()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'truffles':
                    self.resource = Truffles()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'turtles':
                    self.resource = Turtles()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'whales':
                    self.resource = Whales()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'wine':
                    self.resource = Wine()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'horses':
                    self.resource = Horses()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'iron':
                    self.resource = Iron()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'niter':
                    self.resource = Niter()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'coal':
                    self.resource = Coal()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'oil':
                    self.resource = Oil()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'aluminum':
                    self.resource = Aluminum()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

                if name == 'uranium':
                    self.resource = Uranium()
                    terrain_type = str(type(self.terrain)).split('.')[1]
                    feature_type = str(type(self.feature)).split('.')[1]
                    try:
                        if terrain_type not in self.resource.terrain:
                            self.resource = None
                    except AttributeError:
                        pass
                    try:
                        if feature_type not in self.resource.features:
                            self.resource = None
                    except AttributeError:
                        pass

            if name in self.list_of_improvements:
                # print('type is improvement')
                if name == 'farm':
                    self.improvement = Farm()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'mine':
                    self.improvement = Mine()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'quarry':
                    self.improvement = Quarry()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'plantation':
                    self.improvement = Plantation()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'camp':
                    self.improvement = Camp()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'pasture':
                    self.improvement = Pasture()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'fishing_boats':
                    self.improvement = FishingBoats()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'lumber_mill':
                    self.improvement = Lumber_mill()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'fort':
                    self.improvement = Fort()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'airstrip':
                    self.improvement = Airstrip()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'seaside_resort':
                    self.improvement = SeasideResort()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'geothermal_plant':
                    self.improvement = Geothermal_plant()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'wind_farm':
                    self.improvement = Wind_farm()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'solar_farm':
                    self.improvement = Solar_farm()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'offshore_wind_farm':
                    self.improvement = Offshore_wind_farm()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'ski_resort':
                    self.improvement = Ski_resort()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'oil_well':
                    self.improvement = Oil_well()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'offshore_oil_well':
                    self.improvement = Offshore_oil_well()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'missle_silo':
                    self.improvement = Missle_silo()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'mountain_tunnel':
                    self.improvement = Mountain_tunnel()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'railroad':
                    self.improvement = Railroad()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'seastead':
                    self.improvement = Seastead()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'alcazar':
                    self.improvement = Alcazar()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'batey':
                    self.improvement = Batey()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'cahokia_mounds':
                    self.improvement = Cahokia_mounds()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'colossal_heads':
                    self.improvement = Colossal_heads()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'mahavihara':
                    self.improvement = Mahavihara()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'moai':
                    self.improvement = Moai()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'monistary':
                    self.improvement = Monistary()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'nazca_line':
                    self.improvement = Nazca_line()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'trading_dome':
                    self.improvement = Trading_dome()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'chateau':
                    self.improvement = Chateau()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'chemamull':
                    self.improvement = Chemamull()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'golf_course':
                    self.improvement = Golf_course()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'great_wall':
                    self.improvement = Great_wall()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'hacienda':
                    self.improvement = Hacienda()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'ice_hocky_rink':
                    self.improvement = Ice_hocky_rink()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'kampung':
                    self.improvement = Kampung()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'kurgan':
                    self.improvement = Kurgan()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'mekewap':
                    self.improvement = Mekewap()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'mission':
                    self.improvement = Mission()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'nubian_pyramid':
                    self.improvement = Nubian_pyramid()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'open_air_museum':
                    self.improvement = Open_air_museum()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'outback_station':
                    self.improvement = Outback_station()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'pa':
                    self.improvement = Pa()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'pairirdaeza':
                    self.improvement = Pairirdaeza()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'polder':
                    self.improvement = Polder()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'qhapaq_nan':
                    self.improvement = Qhapaq_nan()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'rock_hewn_church':
                    self.improvement = Rock_hewn_church()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'roman_fort':
                    self.improvement = Roman_fort()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'sphinx':
                    self.improvement = Sphinx()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'stepwell':
                    self.improvement = Stepwell()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'terrace_farms':
                    self.improvement = Terrace_farms()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'ziggurat':
                    self.improvement = Ziggurat()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'city_park':
                    self.improvement = City_park()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

                if name == 'fishery':
                    self.improvement = Fishery()
                    try:
                        terrain_type = str(type(self.terrain)).split('.')[1]
                        if terrain_type not in self.improvement.terrain:
                            self.improvement = None
                    except:
                        pass
                    try:
                        feature_type = str(type(self.feature)).split('.')[1]
                        if feature_type not in self.improvement.features:
                            self.improvement = None
                    except:
                        pass
                    try:
                        resource_type = str(type(self.resource)).split('.')[1]
                        if resource_type not in self.improvement.resources:
                            self.improvement = None
                    except:
                        pass

            
            if dist_name[0] in self.list_of_districts:
                if 'city_center' in name:
                    self.district = City_center()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'campus' in name:
                    self.district = Campus()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'theater_square' in name:
                    self.district = Theater_square()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'holy_site' in name:
                    self.district = Holy_site()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'encampment' in name:
                    self.district = Encampment()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'commercial_hub' in name:
                    self.district = Commercial_hub()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'harbor' in name:
                    self.district = Harbor()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'industrial_zone' in name:
                    self.district = Industrial_zone()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'entertainment_complex' in name:
                    self.district = Entertainment_complex()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'water_park' in name:
                    self.district = Water_park()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'aqueduct' in name:
                    self.district = Aqueduct()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'neighborhood' in name:
                    self.district = Neighborhood()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'canal' in name:
                    self.district = Canal()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'dam' in name:
                    self.district = Dam()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'aerodrome' in name:
                    self.district = Aerodrome()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'spaceport' in name:
                    self.district = Spaceport()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'govermment_plaza' in name:
                    self.district = Govermment_plaza()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
                        self.district.set_buildings()

                if 'diplomatic_quarter' in name:
                    self.district = Diplomatic_quarter()
                    try:
                        building = name.split(':')[-1]
                        self.district.set_buildings(building)
                    except:
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


