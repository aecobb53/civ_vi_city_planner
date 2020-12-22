from backend.common_tile import CommonTile

class Copper(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.resource_type = 'bonus'
        self.terrain = [
            'grassland',
            'plains',
            'desert',
            'tundra',
            'snow',
        ]
        self.hills = True
        self.improvement = [
            'mine'
        ]
