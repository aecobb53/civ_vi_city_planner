



class Feature:

    def __init__(self):
        self.food = None
        self.production = None
        self.gold = None
        self.science = None
        self.feature = None

    
    def none(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'None'


    def woods(self):
        """Explanation"""
        self.food = 0
        self.production = 1
        self.gold = 0
        self.science = 0
        self.feature = 'woods'


    def rainforest(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'rainforest'


    def marsh(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'marsh'


    def floodplains(self):
        """Explanation"""
        self.food = 3
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'floodplains'


    def oasis(self):
        """Explanation"""
        self.food = 3
        self.production = 0
        self.gold = 1
        self.science = 0
        self.feature = 'oasis'


    def mountains(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'mountains'


    def cliffs(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'cliffs'


    def reef(self):
        """Explanation"""
        self.food = 1
        self.production = 1
        self.gold = 0
        self.science = 0
        self.feature = 'reef'


    def ice(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'ice'


    def cataract(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'cataract'


    def volcano(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'volcano'


    def volcanic_soil(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 0
        self.feature = 'volcanic_soil'


    def geothermal(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.science = 1
        self.feature = 'geothermal'


    # def river(self):
    #     """Explanation"""
    #     self.food = 0
    #     self.production = 0
    #     self.gold = 0
    #     self.science = 0
    #     self.feature += ' + river'
