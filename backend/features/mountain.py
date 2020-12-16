from common_tile import CommonTile


class Mountain(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'grassland'
        ]
        pass
