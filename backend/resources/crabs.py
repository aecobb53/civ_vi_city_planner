from common_tile import CommonTile

class Crabs(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.resource_type = 'bonus'
        self.terrain = [
            'coast',
            'lake',
        ]
        self.improvement = [
            'fishing_boats'
        ]
