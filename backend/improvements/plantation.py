from backend.common_tile import CommonTile


class Plantation(CommonTile):

    def __init__(self):
        super().__init__()
        self.gold = 2
        self.housing = .5
        self.acceptable_terrain = None
        self.acceptable_features = None
        self.resources = [
            'bananas',
            'citrus',
            'cocoa',
            'coffee',
            'cotton',
            'dyes',
            'silk',
            'sugar',
            'tea',
            'tobacco',
            'wine',
            'olives',
        ]

    def calculate_erah(self, tile_obj, target_index, adj_list):  # pragma: no cover
        target_object = getattr(tile_obj, target_index)
        if tile_obj.erah >= 4:
            target_object.food = target_object.food + 1
        if tile_obj.erah >= 7:
            target_object.gold = target_object.gold + 2
