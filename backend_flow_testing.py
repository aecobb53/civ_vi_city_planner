

from backend.tile_container import Tile
from backend.tile_manager import TileManager

# tile_list = [
#     'grassland',
#     'ice'
# ]

# tc = Tile(tile_list)

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.improvement)

# print("\n-----next one-----\n")

# tile_list = [
#     'grassland',
#     'river',
#     'woods',
#     'hills',
#     'floodplains',
#     'campus',
#     'floodplains',
#     'crabs',
#     'farm',
# ]

# tc = Tile(tile_list)

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# # print('-')
# # print(tc.terrain.food)
# # print(tc.feature.food)

# print("\n-----next one-----\n")

# tile_list = [
#     'grassland',
#     'geothermal_fissure',
#     'geothermal_plant',
# ]

# tc = Tile(tile_list)

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# # print('-')
# # print(tc.terrain.food)
# # print(tc.feature.food)

# print("\n-----next one-----\n")

# tile_list = [
#     'grassland',
#     'hills',
#     'river',
#     'campus',
# ]

# tc = Tile(tile_list)

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# print('-')
# print(tc.terrain.food)
# # print(tc.feature.food)
# print(tc.food)

# print("\n-----next one-----\n")

# tile_list = [
#     'coast',
#     'fish',
#     'fishing_boats'
# ]

# tc = Tile(tile_list)

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

print("\n-----next one-----\n")

tile_list = [
    'grassland',
    'river',
    'woods',
    'hills',
    'floodplains',
    'farm',
]

tc = Tile(tile_list)
tm = TileManager(
    cc=tile_list
)

print(tc.terrain)
print(tc.hills)
print(tc.river)
print(tc.district)
print(tc.feature)
print(tc.resource)
print(tc.improvement)

print('')

# print(tm.__dict__)
print(tm.cc)
print(tm.cc.terrain)
print(tm.cc.terrain.food)
print(tm.cc.food)

tm.calculate_tile_yield('cc')

print(tm.cc)
print(tm.cc.terrain)
print(tm.cc.terrain.food)
print(tm.cc.food)

# tm._zero_out_tile('cc')
tm.calculate_tile_yield('cc')

print(tm.cc)
print(tm.cc.terrain)
print(tm.cc.terrain.food)
print(tm.cc.food)
