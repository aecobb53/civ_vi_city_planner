

class Terrain:

    def __init__(self):
        self.food = None
        self.production = None
        self.gold = None
        self.terrain = None

    
    def none(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.terrain = None


    def grassland(self):
        """Explanation"""
        self.food = 2
        self.production = 0
        self.gold = 0
        self.terrain = 'grassland'


    def grasslandh(self):
        """Explanation"""
        self.food = 2
        self.production = 1
        self.gold = 0
        self.terrain = 'grasslandh'


    def plains(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 0
        self.terrain = 'plains'


    def plainsh(self):
        """Explanation"""
        self.food = 1
        self.production = 1
        self.gold = 0
        self.terrain = 'plainsh'


    def desert(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.terrain = 'desert'


    def deserth(self):
        """Explanation"""
        self.food = 0
        self.production = 1
        self.gold = 0
        self.terrain = 'deserth'


    def tundra(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 0
        self.terrain = 'tundra'


    def tundrah(self):
        """Explanation"""
        self.food = 1
        self.production = 1
        self.gold = 0
        self.terrain = 'tundrah'


    def snow(self):
        """Explanation"""
        self.food = 0
        self.production = 0
        self.gold = 0
        self.terrain = 'snow'


    def snowh(self):
        """Explanation"""
        self.food = 0
        self.production = 1
        self.gold = 0
        self.terrain = 'snowh'


    def coast(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 1
        self.terrain = 'coast'


    def lake(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 1
        self.terrain = 'lake'


    def ocean(self):
        """Explanation"""
        self.food = 1
        self.production = 0
        self.gold = 0
        self.terrain = 'ocean'
