from backend.common_tile import CommonTile


class Airstrip(CommonTile):

    def __init__(self):
        super().__init__()
        self.appeal = -1
        self.acceptable_terrain = None
        self.acceptable_features = None
        self.resources = None
