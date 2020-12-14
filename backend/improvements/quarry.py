from common_tile import CommonTile

class Quarry(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.resources = [
            'stone',
            'marble',
            'gypsum',
        ]
