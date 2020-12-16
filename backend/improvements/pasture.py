from common_tile import CommonTile

class Pasture(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 1
        self.houseing = .5
        self.resources = [
            'sheep',
            'cattle',
            'horses',
        ]
