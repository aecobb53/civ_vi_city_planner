

from backend.tile_container import Tile

tile_list = [
    'grassland',
    'ice'
]

tc = Tile(tile_list)

print(tc.terrain)
print(tc.hills)
print(tc.river)
print(tc.district)
print(tc.feature)
print(tc.improvement)

print("\n-----next one-----\n")

tile_list = [
    'grassland',
    'floodplains'
]

tc = Tile(tile_list)

print(tc.terrain)
print(tc.hills)
print(tc.river)
print(tc.district)
print(tc.feature)
print(tc.improvement)

# print('-')
# print(tc.terrain.food)
# print(tc.feature.food)

