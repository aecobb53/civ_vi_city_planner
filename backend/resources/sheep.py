from backend.common_tile import CommonTile


class Sheep(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.resource_type = 'bonus'
        self.terrain = [
            'grasslandh',
            'plainsh',
            'deserth',
            'tundrah',
        ]
        self.features = None
        self.improvement = [
            'pasture'
        ]
