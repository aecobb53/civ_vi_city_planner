from backend.common_tile import CommonTile


class Hills(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = self.production + 1
