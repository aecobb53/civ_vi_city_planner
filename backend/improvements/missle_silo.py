from backend.common_tile import CommonTile


class MissleSilo(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'desert',
            'grassland',
            'plains',
            'snow',
            'tundra',
        ]
        self.acceptable_features = None
        self.resources = None
