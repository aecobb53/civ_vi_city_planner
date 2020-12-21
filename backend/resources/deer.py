from common_tile import CommonTile

class Deer(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'grassland',
            'plains',
            'tundra',
        ]
        # self.features = [
        #     'woods'
        # ]
        self.improvement = [
            'camp'
        ]
