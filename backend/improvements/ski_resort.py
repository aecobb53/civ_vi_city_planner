from common_tile import CommonTile

class SkiResort(CommonTile):

    def __init__(self):
        super().__init__()
        self.amenities = 1
        self.acceptable_features = [
            'mountains',
        ]

    def calculate_erah(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)
        if target_object.appeal > 0:
            target_object.gold = target_object.gold + target_object.appeal
