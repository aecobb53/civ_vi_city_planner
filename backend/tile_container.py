import yaml

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
        self._hills = None
        self._feature = None
        self._river = None
        self._resource = None
        self._improvement = None
        self._district = None
        self._wonder = None

        # Config
        with open('etc/tile_container.yml') as ycf:
            self.config = yaml.load(ycf, Loader=yaml.FullLoader)
        # print(self.config['features']['list of elements'])
        # print('cataract' in self.config['features']['list of elements'])

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

            # print(f"Now serving: {name}")

            def convert_file_to_object(input):
                """
                Converts a file name to its expected object
                this_file_name becomes ThisFileName
                """
                output = ''.join([i.capitalize() for i in input.split('_')])
                return output

            def object_validation_check(name, conf_element):
                print(name, conf_element)
                # print(self.config[conf_element])
                # print(self.config[conf_element]['list of elements'])
                print(self.config[conf_element]['list of elements'][name])
                # print(self.config[conf_element]['list of elements'][name]['restrictions'])
                # print(self.config[conf_element]['list of elements'][name]['restrictions'])
                if self.config[conf_element]['list of elements'][name] is None:
                    return True
                if self.config[conf_element]['list of elements'][name]['restrictions'] is None:
                    return True

                for restriction in self.config[conf_element]['list of elements'][name]['restrictions']:
                    # print(f"restriction {restriction}")
                    for key, value in restriction.items():
                        # print(f"k,v: {key}, {value}")
                        # print(getattr(self, key))
                        # print(getattr(self, key), value)
                        if getattr(self, key) is None:
                            # print('HERE', value)
                            if value is False:
                                valid = True
                            else:
                                valid = False
                        else:
                            # print('Running the esle statement here')
                            test_val = str(getattr(self, key)).split(' ')[0].split('.')[2]
                            # print(getattr(self, key))
                            # print(test_val)
                            # print(f"{value} = {test_val} ? {value == test_val}")
                            if value == test_val:
                                # print('if is True so valid is True')
                                valid = True
                            elif key == test_val and value:
                                # print('elif is True so valid is True')
                                valid = True
                            else:
                                # print('else is True so valid is False')
                                valid = False
                    if valid:
                        # print(' is valid')
                        return True
                    # else:
                    #     print(' is not valid')
                    #     # return False
                return False

            if name in [i for i in self.config['terrain']['list of elements'] if i not in ['river', 'hills']]:
                if object_validation_check(name, 'terrain'):
                    klass = globals()[convert_file_to_object(name)]
                    self.terrain = klass()

            if name == 'hills':
                # print(f'hills found district:{self.district}')
                if self.district is not None:
                    continue
                if object_validation_check(name, 'terrain'):
                    self.hills = Hills()

            if name == 'river':
                if object_validation_check(name, 'features'):
                    self.river = River()

            # Natural Wonders

            # Wonders

            if name in [i for i in self.config['districts']['list of elements'] if i not in ['river', 'hills']]:
                if object_validation_check(name, 'districts'):
                    klass = globals()[convert_file_to_object(name)]
                    # print('district stuff')
                    # print(name, dist_name)
                    self.district = klass()
                    self.hills = None
                    self.feature = None
                    self.resource = None
                    self.improvement = None
                    if len(dist_name) == 1:
                        self.district.set_buildings()
                    else:
                        print(self.district.building_list)
                        if len(dist_name) == 2:
                            # print('len == 2')
                            self.district.set_buildings(
                                final_improvement=dist_name[1])
                        elif dist_name[2] in ['False', 'false', 'FALSE', False]:
                            # print('is false')
                            self.district.set_buildings(
                                final_improvement=dist_name[1],
                                powered=False)
                        else:
                            # print('else is run')
                            self.district.set_buildings(
                                final_improvement=dist_name[1],
                                powered=True)

                        print(self.district.building_list)

            if name in [i for i in self.config['features']['list of elements'] if i not in ['river', 'hills']]:
                print(f'features run {name}')
                if self.district is not None:
                    print(f"district found not running")
                    continue
                if object_validation_check(name, 'features'):
                    print(f"object validation check passed")
                    klass = globals()[convert_file_to_object(name)]
                    self.feature = klass()

            if name in [i for i in self.config['resources']['list of elements'] if i not in ['river', 'hills']]:
                if self.district is not None:
                    continue
                if object_validation_check(name, 'resources'):
                    klass = globals()[convert_file_to_object(name)]
                    self.resource = klass()

            if name in [i for i in self.config['improvements']['list of elements'] if i not in ['river', 'hills']]:
                if self.district is not None:
                    continue
                if object_validation_check(name, 'improvements'):
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
