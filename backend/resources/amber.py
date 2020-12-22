from backend.common_tile import CommonTile

class Bananas(CommonTile):

    def __init__(self):
        super().__init__()
        self.culture = 1
        self.amenities = 4
        self.resource_type = 'luxury'
        self.terrain = []
        self.features = [
            'woods',
            'rainforest',
            'coast'
        ]
        self.improvement = [
            'mine'
            'fishing_boats'
        ]
