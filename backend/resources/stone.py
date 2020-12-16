from common_tile import CommonTile

class Stone(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'grassland'
        ]
        self.hills = True
        self.improvement = [
            'mine'
        ]
