from common_tile import CommonTile

class FishingBoats(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.houseing = .5
        self.resources = [
            'fish',
            'crabs',
            'whales',
            'pearls',
            'amber',
            'truffles',
        ]
