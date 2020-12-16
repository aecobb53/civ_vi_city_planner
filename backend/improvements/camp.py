from common_tile import CommonTile

class Camp(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.houseing = .5
        self.resources = [
            'deer',
            'furs',
            'ivory',
            'truffles',
            'honey',
        ]
