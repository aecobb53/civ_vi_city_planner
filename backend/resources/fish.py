from backend.common_tile import CommonTile

class Fish(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'coast',
            'lake',
        ]
        self.features = None
        # self.features = [
        #     'reef'
        # ]
        self.improvement = [
            'fishing_boats',
        ]
