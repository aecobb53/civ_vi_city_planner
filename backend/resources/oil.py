from backend.common_tile import CommonTile

class Oil(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 3
        self.resource_type = 'strategic'
        self.terrain = [
            'grassland',
            'desert',
            'trundra',
            'coast',
            'lake',
        ]
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'oil_well'
            'offshore_oil_well'
        ]
