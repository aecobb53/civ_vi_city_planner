from backend.common_tile import CommonTile


class GeothermalPlant(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 2
        self.science = 1
        self.power = 4
        self.acceptable_terrain = None
        self.acceptable_features = [
            'geothermal_fissure',
        ]
        self.resources = None
