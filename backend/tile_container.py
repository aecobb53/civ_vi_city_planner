# from backend.common_tile import CommonTile
# from terrain.grassland import Grassland
# from terrain.plains import Plains
# from features.woods import Woods
# from features.floodplains import Floodplains
# from improvements.farm import Farm
# from districts.campus import Campus
# from resources.bananas import Bananas
# from improvements.plantation import Plantation

from backend.common_tile import CommonTile
from backend.terrain import *
from backend.features import *
from backend.improvements import *
from backend.districts import *
from backend.resources import *


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

            # Terrain
            if name in self.list_of_terrain:
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

            # Features
            if name in self.list_of_features:
                if 'woods' in name:
                    self.feature = Woods()

                if 'rainforest' in name:
                    self.feature = Rainforest()

                if 'marsh' in name:
                    self.feature = Marsh()

                if 'floodplains' in name:
                    self.feature = Floodplains()

                if 'oasis' in name:
                    self.feature = Oasis()

                if 'mountain' in name:
                    self.feature = Mountain()

                if 'cliffs' in name:
                    self.feature = Cliffs()

                if 'reef' in name:
                    self.feature = Reef()

                if 'ice' in name:
                    self.feature = Ice()

                if 'cataract' in name:
                    self.feature = Cataract()

                if 'volcano' in name:
                    self.feature = Volcano()

                if 'volcanic_soil' in name:
                    self.feature = Volcanic_soil()

                if 'geothermal' in name:
                    self.feature = Geothermal()

                terrain_type = str(type(self.terrain)).split('.')[1]
                if terrain_type not in self.feature.acceptable_terrain:
                    self.feature = None

            # River
            if name == 'river':
                self.river = True

            # Resource
            if name in self.list_of_resources:
                if name == 'bananas':
                    self.resource = Bananas()

                if name == 'copper':
                    self.resource = Copper()

                if name == 'cattle':
                    self.resource = Cattle()

                if name == 'crabs':
                    self.resource = Crabs()

                if name == 'deer':
                    self.resource = Deer()

                if name == 'fish':
                    self.resource = Fish()

                if name == 'maize':
                    self.resource = Maize()

                if name == 'rice':
                    self.resource = Rice()

                if name == 'sheep':
                    self.resource = Sheep()

                if name == 'stone':
                    self.resource = Stone()

                if name == 'wheat':
                    self.resource = Wheat()

                if name == 'amber':
                    self.resource = Amber()

                if name == 'cinnamon':
                    self.resource = Cinnamon()

                if name == 'citrus':
                    self.resource = Citrus()

                if name == 'cloves':
                    self.resource = Cloves()

                if name == 'cocoa':
                    self.resource = Cocoa()

                if name == 'coffee':
                    self.resource = Coffee()

                if name == 'cosmetics':
                    self.resource = Cosmetics()

                if name == 'cotton':
                    self.resource = Cotton()

                if name == 'dyes':
                    self.resource = Dyes()

                if name == 'diamonds':
                    self.resource = Diamonds()

                if name == 'furs':
                    self.resource = Furs()

                if name == 'gold_ore':
                    self.resource = Gold_ore()

                if name == 'gypsum':
                    self.resource = Gypsum()

                if name == 'honey':
                    self.resource = Honey()

                if name == 'insense':
                    self.resource = Insense()

                if name == 'ivory':
                    self.resource = Ivory()

                if name == 'jade':
                    self.resource = Jade()

                if name == 'jeans':
                    self.resource = Jeans()

                if name == 'marble':
                    self.resource = Marble()

                if name == 'murcury':
                    self.resource = Murcury()

                if name == 'olives':
                    self.resource = Olives()

                if name == 'pearls':
                    self.resource = Pearls()

                if name == 'perfume':
                    self.resource = Perfume()

                if name == 'salt':
                    self.resource = Salt()

                if name == 'silk':
                    self.resource = Silk()

                if name == 'silver':
                    self.resource = Silver()

                if name == 'spices':
                    self.resource = Spices()

                if name == 'sugar':
                    self.resource = Sugar()

                if name == 'tea':
                    self.resource = Tea()

                if name == 'tobacco':
                    self.resource = Tobacco()

                if name == 'toys':
                    self.resource = Toys()

                if name == 'truffles':
                    self.resource = Truffles()

                if name == 'turtles':
                    self.resource = Turtles()

                if name == 'whales':
                    self.resource = Whales()

                if name == 'wine':
                    self.resource = Wine()

                if name == 'horses':
                    self.resource = Horses()

                if name == 'iron':
                    self.resource = Iron()

                if name == 'niter':
                    self.resource = Niter()

                if name == 'coal':
                    self.resource = Coal()

                if name == 'oil':
                    self.resource = Oil()

                if name == 'aluminum':
                    self.resource = Aluminum()

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

            # Improvements
            if name in self.list_of_improvements:
                if name == 'farm':
                    self.improvement = Farm()

                if name == 'mine':
                    self.improvement = Mine()

                if name == 'quarry':
                    self.improvement = Quarry()

                if name == 'plantation':
                    self.improvement = Plantation()

                if name == 'camp':
                    self.improvement = Camp()

                if name == 'pasture':
                    self.improvement = Pasture()

                if name == 'fishing_boats':
                    self.improvement = FishingBoats()

                if name == 'lumber_mill':
                    self.improvement = LumberMill()

                if name == 'fort':
                    self.improvement = Fort()

                if name == 'airstrip':
                    self.improvement = Airstrip()

                if name == 'seaside_resort':
                    self.improvement = SeasideResort()

                if name == 'geothermal_plant':
                    self.improvement = GeothermalPlant()

                if name == 'wind_farm':
                    self.improvement = WindFarm()

                if name == 'solar_farm':
                    self.improvement = SolarFarm()

                if name == 'offshore_wind_farm':
                    self.improvement = OffshoreWindFarm()

                if name == 'ski_resort':
                    self.improvement = SkiResort()

                if name == 'oil_well':
                    self.improvement = OilWell()

                if name == 'offshore_oil_well':
                    self.improvement = OffshoreOilWell()

                if name == 'missle_silo':
                    self.improvement = MissleSilo()

                if name == 'mountain_tunnel':
                    self.improvement = MountainTunnel()

                if name == 'railroad':
                    self.improvement = Railroad()

                if name == 'seastead':
                    self.improvement = Seastead()

                if name == 'alcazar':
                    self.improvement = Alcazar()

                if name == 'batey':
                    self.improvement = Batey()

                if name == 'cahokia_mounds':
                    self.improvement = CahokiaMounds()

                if name == 'colossal_heads':
                    self.improvement = ColossalHeads()

                if name == 'mahavihara':
                    self.improvement = Mahavihara()

                if name == 'moai':
                    self.improvement = Moai()

                if name == 'monistary':
                    self.improvement = Monistary()

                if name == 'nazca_line':
                    self.improvement = NazcaLine()

                if name == 'trading_dome':
                    self.improvement = TradingDome()

                if name == 'chateau':
                    self.improvement = Chateau()

                if name == 'chemamull':
                    self.improvement = Chemamull()

                if name == 'golf_course':
                    self.improvement = GolfCourse()

                if name == 'great_wall':
                    self.improvement = GreatWall()

                if name == 'hacienda':
                    self.improvement = Hacienda()

                if name == 'ice_hocky_rink':
                    self.improvement = IceHockyRink()

                if name == 'kampung':
                    self.improvement = Kampung()

                if name == 'kurgan':
                    self.improvement = Kurgan()

                if name == 'mekewap':
                    self.improvement = Mekewap()

                if name == 'mission':
                    self.improvement = Mission()

                if name == 'nubian_pyramid':
                    self.improvement = NubianPyramid()

                if name == 'open_air_museum':
                    self.improvement = OpenAirMuseum()

                if name == 'outback_station':
                    self.improvement = OutbackStation()

                if name == 'pa':
                    self.improvement = Pa()

                if name == 'pairirdaeza':
                    self.improvement = Pairirdaeza()

                if name == 'polder':
                    self.improvement = Polder()

                if name == 'qhapaq_nan':
                    self.improvement = QhapaqNan()

                if name == 'rock_hewn_church':
                    self.improvement = RockHewnChurch()

                if name == 'roman_fort':
                    self.improvement = RomanFort()

                if name == 'sphinx':
                    self.improvement = Sphinx()

                if name == 'stepwell':
                    self.improvement = Stepwell()

                if name == 'terrace_farms':
                    self.improvement = TerraceFarms()

                if name == 'ziggurat':
                    self.improvement = Ziggurat()

                if name == 'city_park':
                    self.improvement = CityPark()

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

            # Districts
            if dist_name[0] in self.list_of_districts:
                if 'city_center' in name:
                    self.district = CityCenter()

                if 'campus' in name:
                    self.district = Campus()

                if 'theater_square' in name:
                    self.district = TheaterSquare()

                if 'holy_site' in name:
                    self.district = Holysite()

                if 'encampment' in name:
                    self.district = Encampment()

                if 'commercial_hub' in name:
                    self.district = CommercialHub()

                if 'harbor' in name:
                    self.district = Harbor()

                if 'industrial_zone' in name:
                    self.district = IndustrialZone()

                if 'entertainment_complex' in name:
                    self.district = EntertainmentComplex()

                if 'water_park' in name:
                    self.district = WaterPark()

                if 'aqueduct' in name:
                    self.district = Aqueduct()

                if 'neighborhood' in name:
                    self.district = Neighborhood()

                if 'canal' in name:
                    self.district = Canal()

                if 'dam' in name:
                    self.district = Dam()

                if 'aerodrome' in name:
                    self.district = Aerodrome()

                if 'spaceport' in name:
                    self.district = Spaceport()

                if 'govermment_plaza' in name:
                    self.district = GovermmentPlaza()

                if 'diplomatic_quarter' in name:
                    self.district = DiplomaticQuarter()

                try:
                    building = name.split(':')
                    if len(building) == 1:
                        raise ValueError
                    self.district.set_buildings(building[-1])
                except:
                    self.district.set_buildings()
                self.district.calculate_specialist_yield()

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


