from backend.common_tile import CommonTile


class Mountain(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'desert',
            'grassland',
            'plains',
            'snow',
            'tundra',
        ]
