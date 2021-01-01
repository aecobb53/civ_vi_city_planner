from backend.common_tile import CommonTile


class Iron(CommonTile):

    def __init__(self):
        super().__init__()
        self.science = 1
        self.resource_type = 'strategic'
        self.terrain = [
            'deserth',
            'grasslandh',
            'plainsh',
            'tundrah',
        ]
        self.features = None
        # self.features = [
        #     'rainforest'
        # ]
        self.improvement = [
            'mine',
        ]
