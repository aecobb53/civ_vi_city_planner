from backend.common_tile import CommonTile


class VolcanicSoil(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'desert',
            'deserth',
            'grassland',
            'grasslandh',
            'plains',
            'plainsh',
            'snow',
            'snowh',
            'tundra',
            'tundrah',
        ]
