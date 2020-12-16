from common_tile import CommonTile

class FishingBoats(CommonTile):

    def __init__(self):
        super().__init__()
        self.food = 1
        self.houseing = .5
        self.resources = [
            'fish',
            'crabs',
            'whales',
            'pearls',
            'amber',
            'truffles',
        ]

    def calculate_erah(self, tile_obj, target_index, adj_list):
        target_object = getattr(tile_obj, target_index)
        if tile_obj.erah >= 3:
            target_object.gold = target_object.gold + 2
        if tile_obj.erah >= 4:
            target_object.production = target_object.production + 1
        if tile_obj.erah >= 6:
            target_object.food = target_object.food + 1
