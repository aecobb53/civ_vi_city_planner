from backend.common_tile import CommonTile


class Grassland(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = self.food + 2
