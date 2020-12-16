from common_tile import CommonTile

class SeasideResort(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'coastal',
            'grassland',
            'plains',
            'desert',
        ]
