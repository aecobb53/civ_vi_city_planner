from backend.common_tile import CommonTile


class SeasideResort(CommonTile):

    def __init__(self):
        super().__init__()
        self.acceptable_terrain = [
            'grassland',
            'plains',
            'desert',
        ]
        self.acceptable_features = None
        self.resources = None

    def calculate_erah(self, tile_obj, target_index, adj_list):  # pragma: no cover
        target_object = getattr(tile_obj, target_index)
        if target_object.appeal > 0:
            target_object.gold = target_object.gold + target_object.appeal
