from backend.common_tile import CommonTile

class Cattle(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'grassland',
        ]
        self.features = None
        self.improvement = [
            'pasture',
        ]
