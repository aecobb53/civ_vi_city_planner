from common_tile import CommonTile

class Plantation(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.houseing = .5
        self.resources = [
            'bananas',
            'citrus',
            'cocoa',
            'coffee',
            'cotton',
            'dyes',
            'silk',
            'sugar',
            'tea',
            'tobacco',
            'wine',
            'olives',
        ]
