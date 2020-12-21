from common_tile import CommonTile

class LumberMill(CommonTile):

    def __init__(self):
        super().__init__()
        self.production = 2
        self.acceptable_features = [
            'woods',
            'rainforest',
        ]

    def calculate_erah(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)
        if tile_obj.erah >= 5:
            target_object.production = target_object.production + 1
        if tile_obj.erah >= 8:
            target_object.production = target_object.production + 1
