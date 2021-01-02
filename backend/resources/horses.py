from backend.common_tile import CommonTile


class Horses(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.production = 1
        self.resource_type = 'strategic'
        self.terrain = [
            'grassland',
            'plains'
        ]
        self.features = None
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'pasture'
        ]
