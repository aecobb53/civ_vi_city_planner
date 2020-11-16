tile = {
  'Terrain': {
    'None': [0,0,0],
    'Grassland': [2,0,0],
    'GrasslandH': [2,1,0],
    'Plains': [1,0,0],
    'PlainsH': [1,1,0],
    'Desert': [0,0,0],
    'DesertH': [0,1,0],
    'Tundra': [1,0,0],
    'TundraH': [1,1,0],
    'Snow': [0,0,0],
    'SnowH': [0,1,0],
    'Coast': [1,0,1],
    'Lake': [1,0,1],
    'Ocean': [1,0,0]
  },
  'Features': {
    'None': [0,0,0],
    'Woods': [0,1,0],
    'Rainforest': [1,0,0],
    'Marsh': [1,0,0],
    'River': [0,0,0],
    'Floodplains': [3,0,0],
    'Oasis': [3,0,1],
    'Mountains': [0,0,0],
    'Cliffs': [0,0,0],
    'Reef': [1,1,0],
    'Ice': [0,0,0],
    'Cataract': [0,0,0],
    'Volcano': [0,0,0],
    'Colcanic': [0,0,0],
    'Geothermal': [0,0,0]
  }
}

city = {
  'city': [0],
  'inner': list(range(0,6)),
  'midde': list(range(0,12)),
  'outer': list(range(0,18))
}

for k1,v1 in tile.items():
  for k2,v2 in v1.items():
    print(k1,k2,v2)
#print(tile)