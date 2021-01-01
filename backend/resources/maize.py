from backend.common_tile import CommonTile


class Maize(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.resource_type = 'bonus'
        self.terrain = [
            'grasssland',
            'plains',
        ]
        self.features = None
        # self.features = [
        #     'floodplains'
        # ]
        self.improvement = [
            'farm',
        ]
