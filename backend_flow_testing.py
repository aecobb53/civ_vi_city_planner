

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

# print('-')
# print(tc.terrain.food)
# print(tc.feature.food)

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
#     'hills',
#     'river'
# ]

# tc = Tile(tile_list)
# tm = TileManager(
#     cc=tile_list
# )
# tm.calculate_tile_yield('cc')

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# print("\n-----next one-----\n")

# tile_list = [
#     'grassland',
#     'river',
#     'woods',
#     'hills',
#     'floodplains',
#     'farm',
# ]

# tc = Tile(tile_list)
# tm = TileManager(
#     cc=tile_list
# )

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# print('')

# # print(tm.__dict__)
# print(tm.cc)
# print(tm.cc.terrain)
# print(tm.cc.terrain.food)
# print(tm.cc.food)
# print(tm.cc.production)

# tm.calculate_tile_yield('cc')

# print(tm.cc)
# print(tm.cc.terrain)
# print(tm.cc.terrain.food)
# print(tm.cc.food)
# print(tm.cc.production)

# # tm._zero_out_tile('cc')
# tm.calculate_tile_yield('cc')

# print(tm.cc)
# print(tm.cc.terrain)
# print(tm.cc.terrain.food)
# print(tm.cc.food)
# print(tm.cc.production)

# print("\n-----next one-----\n")

# tile_list = [
#     'grassland',
#     'river',
#     'woods',
#     'hills',
#     'floodplains',
#     'farm',
#     # 'campus'
#     # 'campus:1'
#     # 'campus:university'
#     'campus'
# ]

# tc = Tile(tile_list)
# tm = TileManager(
#     cc=tile_list
# )

# print(tc.terrain)
# print(tc.hills)
# print(tc.river)
# print(tc.district)
# print(tc.feature)
# print(tc.resource)
# print(tc.improvement)

# print('')

# # print(tm.__dict__)
# print(tm.cc.science)
# print(tm.cc.district.powered)
# print(tm.cc.district.science)
# print(tm.cc.district.building_list)

# # tm.calculate_tile_yield('cc')
# # print('')

# # print(tm.cc.science)
# # print(tm.cc.district.powered)
# # print(tm.cc.district.science)
# # print(tm.cc.district.building_list)

# # tm.cc.district.calculate_adjacency(tm, 'cc', [])
# # tm.cc.district.calculate_specialist_yield()
# tm.calculate_tile_yield('cc')
# print('')

# print(tm.cc.science)
# print(tm.cc.district.powered)
# print(tm.cc.district.science)
# print(tm.cc.district.building_list)

print("\n-----next one-----\n")

tile_list = [
    'grassland',
    # 'campus'
    # 'campus:1'
    # 'campus:university'
    'campus'
]
tile_list2 = [
    'grassland',
    'mountains'
]

tc = Tile(tile_list)
tc2 = Tile(tile_list2)
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
print(tc2.terrain)
print(tc2.hills)
print(tc2.river)
print(tc2.district)
print(tc2.feature)
print(tc2.resource)
print(tc2.improvement)

print('')

# print(tm.__dict__)
print(tm.cc.science)
print(tm.cc.district.powered)
print(tm.cc.district.science)
print(tm.cc.district.building_list)

# tm.calculate_tile_yield('cc')
# print('')

# print(tm.cc.science)
# print(tm.cc.district.powered)
# print(tm.cc.district.science)
# print(tm.cc.district.building_list)

tm.cc.district.calculate_adjacency(tm, 'cc', [])
tm.cc.district.calculate_specialist_yield()
# tm.calculate_tile_yield('cc')
print('')

print(tm.cc.science)
print(tm.cc.district.powered)
print(tm.cc.district.science)
print(tm.cc.district.building_list)