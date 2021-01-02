from backend.common_tile import CommonTile


class Aluminum(CommonTile):

    def __init__(self):
        super().__init__()
        self.science = 1
        self.resource_type = 'strategic'
        self.terrain = [
            'desert',
            'plains',
        ]
        self.features = None
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'mine',
        ]
