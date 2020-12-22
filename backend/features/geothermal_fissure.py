from backend.common_tile import CommonTile


class GeothermalFissure(CommonTile):

    def __init__(self):
        super().__init__()
        self.science = 1
        self.acceptable_terrain = [
            'grassland',
            'plains',
            'desert',
            'tundra',
            'snow',
        ]
