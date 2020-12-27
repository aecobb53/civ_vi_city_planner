from backend.common_tile import CommonTile


class Ice(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'coast',
            'ocean',
        ]
