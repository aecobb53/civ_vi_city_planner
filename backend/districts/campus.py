from common_tile import CommonTile

class Campus(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'library',
            'university',
            'research_lab',
        ]
        self._building_list = None
        self._library = None
        self._university = None
        self._research_lab = None
        self._powered = None
        self._power = None

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement == None:
            self.powered = True
            # print(self.powered)
            final_improvement = 'research_lab'
        if isinstance(final_improvement, int):
            final_improvement = self.default_building_list[final_improvement]

        if powered:
            self.powered = True

        for building in self.default_building_list:
            if building == final_improvement:
                setattr(self, building, True)
                break
            else:
                setattr(self, building, True)


    # building_list
    @property
    def building_list(self):
        if self._building_list == None:
            return None
        return self._building_list

    # @building_list.setter
    def update_building_list(self, value):
        if self._building_list == None:
            self._building_list = []
        self._building_list.append(value)

    # library
    @property
    def library(self):
        if self._library == None:
            return None
        return self._library

    @library.setter
    def library(self, value):
        if value == True:
            self.science = self.science + 2
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('library')
            self._library = True

    # university
    @property
    def university(self):
        if self._university == None:
            return None
        return self._university

    @university.setter
    def university(self, value):
        if value == True:
            self.science = self.science + 4
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('university')
            self._university = True

    # research_lab
    @property
    def research_lab(self):
        if self._research_lab == None:
            return None
        return self._research_lab

    @research_lab.setter
    def research_lab(self, value):
        if value == True:
            self.science = self.science + 3
            if self.powered:
                self.science = self.science + 5
            self.houseing = self.houseing + 1
            self.citizen_slot = self.citizen_slot + 1
            self.update_building_list('research_lab')
            self._research_lab = True

    # power
    @property
    def power(self):
        if self._power == None:
            return 0
        self._power

    @power.setter
    def power(self, value):
        self._power = value

    # powered
    @property
    def powered(self):
        if self._powered == None:
            return False
        self._powered

    @powered.setter
    def powered(self, value):
        self._power = 3
        self._powered = value

