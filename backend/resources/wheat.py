from common_tile import CommonTile

class Wheat(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'plains',
            'desert',
        ]
        # self.features = [
        #     'floodplains'
        # ]
        self.improvement = [
            'plantation'
        ]
