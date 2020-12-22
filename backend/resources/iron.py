from backend.common_tile import CommonTile

class Iron(CommonTile):

    def __init__(self):
        super().__init__()
        self.science = 1
        self.resource_type = 'strategic'
        self.terrain = [
            'desert',
            'grassland',
            'plains',
            'tundra',
        ]
        self.hills = True
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'mine'
        ]
