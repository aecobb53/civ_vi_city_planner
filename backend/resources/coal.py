from common_tile import CommonTile

class Coal(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 2
        self.resource_type = 'strategic'
        self.terrain = [
            'grassland',
            'plains',
        ]
        self.hills = True
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'mine'
        ]
