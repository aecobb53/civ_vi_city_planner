from backend.common_tile import CommonTile
import math


class GovernmentPlaza(CommonTile):

    def __init__(self):
        super().__init__()
        self.default_building_list = [
            'ancestral_hall',
            'audience_chamber',
            'warlords_throne',
            'foreign_ministry',
            'grand_masters_chapel',
            'intelligence_agency',
            'national_history_museum',
            'royal_society',
            'war_department',
        ]
        self._building_list = None
        self._ancestral_hall = None
        self._audience_chamber = None
        self._warlords_throne = None
        self._foreign_ministry = None
        self._grand_masters_chapel = None
        self._intelligence_agency = None
        self._national_history_museum = None
        self._royal_society = None
        self._war_department = None
        self._powered = None
        self._power = None
        self.maintenance = self.maintenance + 1

    # building_list
    @property
    def building_list(self):
        if self._building_list is None:
            return None
        return self._building_list

    # @building_list.setter
    def update_building_list(self, value):
        if self._building_list is None:
            self._building_list = []
        self._building_list.append(value)

    def remove_building_list(self, value):
        if self._building_list == None:
            return None
        self._building_list.remove(value)

    # Tier I
    # ancestral_hall
    @property
    def ancestral_hall(self):
        if self._ancestral_hall is None:
            return False
        return self._ancestral_hall

    @ancestral_hall.setter
    def ancestral_hall(self, value):
        if value:
            self.maintenance = self.maintenance + 1
            self.update_building_list('ancestral_hall')
            self._ancestral_hall = True
            if self.audience_chamber:
                del self.audience_chamber
            if self.warlords_throne:
                del self.warlords_throne

    @ancestral_hall.deleter
    def ancestral_hall(self):
        if self._ancestral_hall:
            self.maintenance = self.maintenance - 1
            self.remove_building_list('ancestral_hall')
            self._ancestral_hall = None
            
    # audience_chamber
    @property
    def audience_chamber(self):
        if self._audience_chamber is None:
            return False
        return self._audience_chamber

    @audience_chamber.setter
    def audience_chamber(self, value):
        if value:
            self.maintenance = self.maintenance + 1
            self.update_building_list('audience_chamber')
            self._audience_chamber = True
            if self.ancestral_hall:
                del self.ancestral_hall
            if self.warlords_throne:
                del self.warlords_throne

    @audience_chamber.deleter
    def audience_chamber(self):
        if self._audience_chamber:
            self.maintenance = self.maintenance - 1
            self.remove_building_list('audience_chamber')
            self._audience_chamber = None
            
    # warlords_throne
    @property
    def warlords_throne(self):
        if self._warlords_throne is None:
            return False
        return self._warlords_throne

    @warlords_throne.setter
    def warlords_throne(self, value):
        if value:
            self.maintenance = self.maintenance + 1
            self.update_building_list('warlords_throne')
            self._warlords_throne = True
            if self.ancestral_hall:
                del self.ancestral_hall
            if self.audience_chamber:
                del self.audience_chamber

    @warlords_throne.deleter
    def warlords_throne(self):
        if self._warlords_throne:
            self.maintenance = self.maintenance - 1
            self.remove_building_list('warlords_throne')
            self._warlords_throne = None
            
    # Tier II
    # foreign_ministry
    @property
    def foreign_ministry(self):
        if self._foreign_ministry is None:
            return False
        return self._foreign_ministry

    @foreign_ministry.setter
    def foreign_ministry(self, value):
        if value:
            self.maintenance = self.maintenance + 2
            self.update_building_list('foreign_ministry')
            self._foreign_ministry = True
            if self.grand_masters_chapel:
                del self.grand_masters_chapel
            if self.intelligence_agency:
                del self.intelligence_agency

    @foreign_ministry.deleter
    def foreign_ministry(self):
        if self._foreign_ministry:
            self.maintenance = self.maintenance - 2
            self.remove_building_list('foreign_ministry')
            self._foreign_ministry = None
            
    # grand_masters_chapel
    @property
    def grand_masters_chapel(self):
        if self._grand_masters_chapel is None:
            return False
        return self._grand_masters_chapel

    @grand_masters_chapel.setter
    def grand_masters_chapel(self, value):
        if value:
            self.maintenance = self.maintenance + 2
            self.faith = self.faith + 5
            self.update_building_list('grand_masters_chapel')
            self._grand_masters_chapel = True
            if self.foreign_ministry:
                del self.foreign_ministry
            if self.intelligence_agency:
                del self.intelligence_agency

    @grand_masters_chapel.deleter
    def grand_masters_chapel(self):
        if self._grand_masters_chapel:
            self.maintenance = self.maintenance - 2
            self.faith = self.faith - 5
            self.remove_building_list('grand_masters_chapel')
            self._grand_masters_chapel = None
            
    # intelligence_agency
    @property
    def intelligence_agency(self):
        if self._intelligence_agency is None:
            return False
        return self._intelligence_agency

    @intelligence_agency.setter
    def intelligence_agency(self, value):
        if value:
            self.maintenance = self.maintenance + 2
            self.update_building_list('intelligence_agency')
            self._intelligence_agency = True
            if self.foreign_ministry:
                del self.foreign_ministry
            if self.grand_masters_chapel:
                del self.grand_masters_chapel

    @intelligence_agency.deleter
    def intelligence_agency(self):
        if self._intelligence_agency:
            self.maintenance = self.maintenance - 2
            self.remove_building_list('intelligence_agency')
            self._intelligence_agency = None
            
    # Tier III
    # national_history_museum
    @property
    def national_history_museum(self):
        if self._national_history_museum is None:
            return False
        return self._national_history_museum

    @national_history_museum.setter
    def national_history_museum(self, value):
        if value:
            self.maintenance = self.maintenance + 3
            self.update_building_list('national_history_museum')
            self._national_history_museum = True
            if self.royal_society:
                del self.royal_society
            if self.war_department:
                del self.war_department

    @national_history_museum.deleter
    def national_history_museum(self):
        if self._national_history_museum:
            self.maintenance = self.maintenance - 3
            self.remove_building_list('national_history_museum')
            self._national_history_museum = None
            
    # royal_society
    @property
    def royal_society(self):
        if self._royal_society is None:
            return False
        return self._royal_society

    @royal_society.setter
    def royal_society(self, value):
        if value:
            self.maintenance = self.maintenance + 3
            self.update_building_list('royal_society')
            self._royal_society = True
            if self.national_history_museum:
                del self.national_history_museum
            if self.war_department:
                del self.war_department

    @royal_society.deleter
    def royal_society(self):
        if self._royal_society:
            self.maintenance = self.maintenance - 3
            self.remove_building_list('royal_society')
            self._royal_society = None
            
    # war_department
    @property
    def war_department(self):
        if self._war_department is None:
            return False
        return self._war_department

    @war_department.setter
    def war_department(self, value):
        if value:
            self.maintenance = self.maintenance + 3
            self.update_building_list('war_department')
            self._war_department = True
            if self.national_history_museum:
                del self.national_history_museum
            if self.royal_society:
                del self.royal_society

    @war_department.deleter
    def war_department(self):
        if self._war_department:
            self.maintenance = self.maintenance - 3
            self.remove_building_list('war_department')
            self._war_department = None
            
    # power - Whats the power draw
    @property
    def power(self):
        if self._power is None:
            return False
        return self._power

    @power.setter
    def power(self, value):
        pass
        # self._power = value

    # powered - Does the city need power?
    @property
    def powered(self):
        if self._powered is None:
            return False
        return self._powered

    @powered.setter
    def powered(self, value):
        # self.power = 3
        # self._powered = value
        pass

    def set_buildings(
        self,
        final_improvement=None,
        powered=None):

        if final_improvement is None:
            powered = True
            final_improvement = 'royal_society'
        try:
            final_improvement = int(final_improvement)
        except:
            pass
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

    def calculate_adjacency(self, tile_obj, target_index, adj_list):
        pass

    def calculate_specialist_yield(self):
        pass
