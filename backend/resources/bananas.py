from common_tile import CommonTile

class Bananas(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.terrain = []
        self.features = []
        self.improvement = 'plantation'
