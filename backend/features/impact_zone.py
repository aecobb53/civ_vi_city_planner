from common_tile import CommonTile


class ImpactZone(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'grassland',
            'plains',
            'desert',
            'tundra',
            'snow',
        ]
        self.hills = True
