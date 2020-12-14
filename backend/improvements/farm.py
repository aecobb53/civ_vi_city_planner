from common_tile import CommonTile

class Farm(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.production = 0
        self.gold = 0
        self.houseing = .5
        self.acceptable_terrain = [
            'grassland',
            'plains',
        ]
        self.acceptable_features = [
            'floodplains'
        ]
        self.resources = [
            'wheat',
            'rice',
            'maize',
        ]
        self.hills = True
