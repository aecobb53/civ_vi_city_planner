from common_tile import CommonTile

class Bananas(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.resource_type = 'bonus'
        self.terrain = []
        self.features = [
            'rainforest'
        ]
        self.improvement = [
            'plantation'
        ]
