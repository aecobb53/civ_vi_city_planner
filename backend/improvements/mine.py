from backend.common_tile import CommonTile

class Mine(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.appeal = -1
        self.acceptable_terrain = [
            'deserth',
            'grasslandh',
            'plainsh',
            'snowh',
            'tundrah',
        ]
        self.acceptable_features = None
        self.resources = [
            'copper',
            'diamonds',
            'gold_ore',
            'iron',
            'jade',
            'mercury',
            'salt',
            'niter',
            'coal',
            'aluminum',
            'uranium',
            'amber',
        ]


    def calculate_erah(self, tile_obj, target_index, adj_list):  # pragma: no cover
        target_object = getattr(tile_obj, target_index)
        if tile_obj.erah >= 2:
            target_object.production = target_object.production + 1
        if tile_obj.erah >= 4:
            target_object.production = target_object.production + 1
