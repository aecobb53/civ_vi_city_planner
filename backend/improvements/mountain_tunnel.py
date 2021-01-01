from backend.common_tile import CommonTile

class MountainTunnel(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = None
        self.acceptable_features = [
            'mountain',
        ]
        self.resources = None
