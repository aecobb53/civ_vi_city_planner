from backend.common_tile import CommonTile


class Pasture(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 1
        self.housing = .5
        self.acceptable_terrain = None
        self.acceptable_features = None
        self.resources = [
            'sheep',
            'cattle',
            'horses',
        ]

    # Has an adjacency bonus but needs to account for special improvement outback station

    def calculate_erah(self, tile_obj, target_index, adj_list):  # pragma: no cover
        target_object = getattr(tile_obj, target_index)
        if tile_obj.erah >= 2:
            target_object.food = target_object.food + 1
        if tile_obj.erah >= 5:
            target_object.production = target_object.production + 1
        if tile_obj.erah >= 7:
            target_object.production = target_object.production + 1
