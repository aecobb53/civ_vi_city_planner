from common_tile import CommonTile

class Mine(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.acceptable_terrain = [
            'desert',
            'grassland',
            'plains',
            'snow',
            'tundra',
        ]
        self.resources = [
            'copper',
            'diamonds',
            'gold_ore',
            'iron',
            'jade',
            'mercury',
            'salt',
            'niter',
            'coal',
            'aluminum',
            'uranium',
            'amber',
        ]
        self.hills = True
