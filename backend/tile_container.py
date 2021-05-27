import yaml

from backend.common_tile import CommonTile
from backend.terrain import *
from backend.features import *
from backend.improvements import *
from backend.districts import *
from backend.resources import *

from backend.bin.logger import Logger


class Tile(CommonTile):
    """
    This manages the aspects of a tile. Simple things like ther can only be one terrain feature.
    """

    def __init__(
        self,
        tile_list):
        super().__init__()
        self._terrain = None
        self._hills = None
        self._feature = None
        self._river = None
        self._resource = None
        self._improvement = None
        self._district = None
        self._wonder = None
        self.logger = Logger(
            'tile_container',
            log_directory='logs/backend/',
            app_name_in_file=True,
            # log_suffix=log_prefix,
            # log_prefix='main',
            date_in_file=False,
            time_in_file=False,
            utc_in_file=False,
            f_level='DEBUG',
            c_level='WARNING')
        self.logit = self.logger.return_logit()

        # Config
        with open('etc/tile_container.yml') as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)
        # self.logit.debug('new container created')

        for name in tile_list:
            # First i need to make sure the order of everything is correct
            if ':' in name:
                """
                If i want specific buildings in a district i append the district with a :building name or :building_number
                ex: campus
                ex: campus:2
                ex: campus:univeristy
                ex: campus:2:True
                ex: campus:2:False
                ex: campus:univeristy:True
                ex: campus:univeristy:False
                """
                dist_name = name.split(':')
                name = name.split(':')[0]
            else:
                dist_name = [name]

            self.logit.debug(f"Now serving: {name}")

            def convert_file_to_object(input):
                """
                Converts a file name to its expected object
                this_file_name becomes ThisFileName
                """
                output = ''.join([i.capitalize() for i in input.split('_')])
                return output

            def object_validation_check(name, conf_element):
                self.logit.debug(f"name:{name}, element type:{conf_element}")
                try:
                    self.logit.debug(f"list of elements:{self.config[conf_element]['list of elements'][name]['restrictions']}")
                except TypeError:
                    self.logit.debug(f"type is terrain")
                if self.config[conf_element]['list of elements'][name] is None:
                    return True
                if self.config[conf_element]['list of elements'][name]['restrictions'] is None:
                    return True

                for restriction in self.config[conf_element]['list of elements'][name]['restrictions']:
                    self.logit.debug(f"considering restriction:{restriction}")
                    for key, value in restriction.items():
                        self.logit.debug(f"k,v: {key}, {value}")
                        if getattr(self, key) is None:
                            if value is False:
                                valid = True
                                self.logit.debug('type is None and desired')
                            else:
                                valid = False
                                self.logit.debug('type is None and NOT desired')
                        else:
                            test_val = str(getattr(self, key)).split(' ')[0].split('.')[2]
                            self.logit.debug(f"test string:{test_val} against value:{value}")
                            if value == test_val:
                                self.logit.debug(f"value == testval")
                                valid = True
                            elif key == test_val and value:
                                self.logit.debug(f"key == test_val and value == True")
                                valid = True
                            else:
                                self.logit.debug(f"test_val != value or key")
                                valid = False
                    if valid:
                        self.logit.debug('valid is Ture, returning True')
                        return True
                self.logit('valid is False, returning False')
                return False

            if name in [i for i in self.config['terrain']['list of elements'] if i not in ['river', 'hills']]:
                if object_validation_check(name, 'terrain'):
                    klass = globals()[convert_file_to_object(name)]
                    self.logit.debug(f"Name:{name} is a terrain object and created {klass}")
                    self.terrain = klass()

            if name == 'hills':
                if self.district is not None:
                    continue
                if object_validation_check(name, 'terrain'):
                    self.logit.debug(f"Name:{name} is a hills object and will create Hills")
                    self.hills = Hills()

            if name == 'river':
                if object_validation_check(name, 'features'):
                    self.logit.debug(f"Name:{name} is a river object and will create River")
                    self.river = River()

            # Natural Wonders

            # Wonders

            if name in [i for i in self.config['districts']['list of elements'] if i not in ['river', 'hills']]:
                if object_validation_check(name, 'districts'):
                    klass = globals()[convert_file_to_object(name)]
                    self.logit.debug(f"Name:{dist_name} is a district object and created {klass}")
                    self.district = klass()
                    self.hills = None
                    self.feature = None
                    self.resource = None
                    self.improvement = None
                    if len(dist_name) == 1:
                        self.logit.debug('no district extention, using defaults')
                        self.district.set_buildings()
                    else:
                        if len(dist_name) == 2:
                            self.logit.debug(f"district building set to {dist_name[1]}")
                            self.district.set_buildings(
                                final_improvement=dist_name[1])
                        elif dist_name[2] in ['False', 'false', 'FALSE', False]:
                            self.logit.debug(f"dist_name[2] is a False type")
                            self.district.set_buildings(
                                final_improvement=dist_name[1],
                                powered=False)
                        else:
                            self.logit.debug(f"No false, dist_name[1] is {dist_name[1]}")
                            self.district.set_buildings(
                                final_improvement=dist_name[1],
                                powered=True)

                    self.logit.debug(f"district building list:{self.district.building_list}")

            if name in [i for i in self.config['features']['list of elements'] if i not in ['river', 'hills']]:
                if self.district is not None:
                    continue
                if object_validation_check(name, 'features'):
                    self.logit.debug(f"Name:{name} is a feature object and created {klass}")
                    klass = globals()[convert_file_to_object(name)]
                    self.feature = klass()

            if name in [i for i in self.config['resources']['list of elements'] if i not in ['river', 'hills']]:
                if self.district is not None:
                    continue
                if object_validation_check(name, 'resources'):
                    self.logit.debug(f"Name:{name} is a resource object and created {klass}")
                    klass = globals()[convert_file_to_object(name)]
                    self.resource = klass()

            if name in [i for i in self.config['improvements']['list of elements'] if i not in ['river', 'hills']]:
                if self.district is not None:
                    continue
                if object_validation_check(name, 'improvements'):
                    self.logit.debug(f"Name:{name} is a improvement object and created {klass}")
                    klass = globals()[convert_file_to_object(name)]
                    self.improvement = klass()

    # terrain
    @property
    def terrain(self):
        if self._terrain is None:
            return None
        return self._terrain

    @terrain.setter
    def terrain(self, value):
        self._terrain = value

    # hills
    @property
    def hills(self):
        if self._hills is None:
            return None
        return self._hills

    @hills.setter
    def hills(self, value):
        self._hills = value

    # feature
    @property
    def feature(self):
        if self._feature is None:
            return None
        return self._feature

    @feature.setter
    def feature(self, value):
        self._feature = value

    # river
    @property
    def river(self):
        if self._river is None:
            return None
        return self._river

    @river.setter
    def river(self, value):
        self._river = value

    # resource
    @property
    def resource(self):
        if self._resource is None:
            return None
        return self._resource

    @resource.setter
    def resource(self, value):
        self._resource = value

    # improvement
    @property
    def improvement(self):
        if self._improvement is None:
            return None
        return self._improvement

    @improvement.setter
    def improvement(self, value):
        self._improvement = value

    # district
    @property
    def district(self):
        if self._district is None:
            return None
        return self._district

    @district.setter
    def district(self, value):
        self._district = value

    # wonder
    @property
    def wonder(self):
        if self._wonder is None:
            return None
        return self._wonder

    @wonder.setter
    def wonder(self, value):
        self._wonder = value
