from common_tile import CommonTile

class SkiResort(CommonTile):

    def __init__(self):
        super().__init__()
        self.amenities = 1
        self.acceptable_features = [
            'mountains',
        ]
