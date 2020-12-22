from backend.common_tile import CommonTile


class Marsh(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.acceptable_terrain = [
            'grassland'
        ]