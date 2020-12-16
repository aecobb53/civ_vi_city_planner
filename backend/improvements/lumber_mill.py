from common_tile import CommonTile

class LumberMill(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 2
        self.acceptable_features = [
            'woods',
            'rainforest',
        ]
