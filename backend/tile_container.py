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
            # if ':' in name:
            #     """
            #     If i want specific buildings in a district i append the district with a :building name or :building_number
            #     ex: campus
            #     ex: campus:2
            #     ex: campus:univeristy
            #     """
            #     dist_name = name.split(':')
            # else:
            #     dist_name = [name]

            print(f"Now serving: {name}")

            def convert_file_to_object(input):
                """
                Converts a file name to its expected object
                this_file_name becomes ThisFileName
                """
                output = ''.join([i.capitalize() for i in input.split('_')])
                return output

            if name in self.config['terrain']['list of elements']:
                klass = globals()[convert_file_to_object(name)]
                self.terrain = klass()

            if name == 'hills':
                self.hills = Hills()

            if name == 'river':
                self.river = River()

            # Natural Wonders

            # Wonders

            if name in self.config['districts']['list of elements']:
                # self.tile_parts['districts'] = name
                pass

            if name in self.config['features']['list of elements']:
                klass = globals()[convert_file_to_object(name)]

                print(self.config['features']['list of elements'][name]['restrictions'])

                if self.config['features']['list of elements'][name]['restrictions'] is None:
                    self.feature = klass()
                    return

                for restriction in self.config['features']['list of elements'][name]['restrictions']:
                    print(f"restriction {restriction}")
                    for key, value in restriction.items():
                        print(f"k,v: {key}, {value}")
                        # print(getattr(self, key))
                        print(getattr(self, key), value)
                        if getattr(self, key) is None:
                            if value is False:
                                valid = True
                            else:
                                valid = False
                        else:
                            print('Running the esle statement here')
                            test_val = str(getattr(self, key)).split(' ')[0].split('.')[2]
                            print(getattr(self, key))
                            print(test_val)
                            print(f"{value} = {test_val} ? {value == test_val}")
                            if value == test_val:
                                valid = True
                            else:
                                valid = False
                    # Here is whereI would accept a valid match if valid == true else not a match and continue. 
                # If end of list and still valid ==  false dont assing feature
                self.feature = klass()

            if name in self.config['resources']['list of elements']:
                klass = globals()[convert_file_to_object(name)]
                self.resource = klass()

            if name in self.config['improvements']['list of elements']:
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
