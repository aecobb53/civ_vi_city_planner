from backend.common_tile import CommonTile

class OffshoreOilRig(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 2
        self.appeal = -1
        self.resources = [
            'oil',
        ]
