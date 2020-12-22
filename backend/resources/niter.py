from backend.common_tile import CommonTile

class Niter(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.production = 1
        self.resource_type = 'strategic'
        self.terrain = [
            'desert',
            'grassland',
            'plains',
            'tundra',
        ]
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'mine'
        ]
