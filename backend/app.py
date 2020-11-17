import terrain
import feature
import improvement
# import adjacency
import district


class CivVI:

    def __init__(self):

        self.tiles = {}
        self.game = {}
        self.city = {}

        example = { 'terrain':None, 'feature':None, 'river':None, 'natural_wonder':None,
                    'improvement':None, 'district':None, 'wonder':None,
                    'adjacency':None, 'set':False,}

        self.erahs = {
            'Ancient':0,
            'Classical':1,
            'Medieval':2,
            'Renaissance':3,
            'Industrial':4,
            'Modern':5,
            'Atomic':6,
            'Information':7,
            'Future':8,
        }

        self.tiles['cc'] = example.copy()
        self.tiles['i0'] = example.copy()
        self.tiles['i1'] = example.copy()
        self.tiles['i2'] = example.copy()
        self.tiles['i3'] = example.copy()
        self.tiles['i4'] = example.copy()
        self.tiles['i5'] = example.copy()
        self.tiles['m0'] = example.copy()
        self.tiles['m1'] = example.copy()
        self.tiles['m2'] = example.copy()
        self.tiles['m3'] = example.copy()
        self.tiles['m4'] = example.copy()
        self.tiles['m5'] = example.copy()
        self.tiles['m6'] = example.copy()
        self.tiles['m7'] = example.copy()
        self.tiles['m8'] = example.copy()
        self.tiles['m9'] = example.copy()
        self.tiles['m10'] = example.copy()
        self.tiles['m11'] = example.copy()
        self.tiles['o0'] = example.copy()
        self.tiles['o1'] = example.copy()
        self.tiles['o2'] = example.copy()
        self.tiles['o3'] = example.copy()
        self.tiles['o4'] = example.copy()
        self.tiles['o5'] = example.copy()
        self.tiles['o6'] = example.copy()
        self.tiles['o7'] = example.copy()
        self.tiles['o8'] = example.copy()
        self.tiles['o9'] = example.copy()
        self.tiles['o10'] = example.copy()
        self.tiles['o11'] = example.copy()
        self.tiles['o12'] = example.copy()
        self.tiles['o13'] = example.copy()
        self.tiles['o14'] = example.copy()
        self.tiles['o15'] = example.copy()
        self.tiles['o16'] = example.copy()
        self.tiles['o17'] = example.copy()

        self.tiles['cc']['adjacency_members'] = ['i0','i1','i2','i3','i4','i5']
        self.tiles['i0']['adjacency_members'] = ['m0','m1','i1','cc','i5','m11']
        self.tiles['i1']['adjacency_members'] = ['m1','m2','m3','i2','cc','i0']
        self.tiles['i2']['adjacency_members'] = ['i1','m3','m4','m5','i3','cc']
        self.tiles['i3']['adjacency_members'] = ['cc','i2','m5','m6','m7','i4']
        self.tiles['i4']['adjacency_members'] = ['i5','cc','i3','m7','m8','m9']
        self.tiles['i5']['adjacency_members'] = ['m11','i0','cc','i4','m9','m10']
        self.tiles['m0']['adjacency_members'] = ['o0','o1','m1','i0','m11','o17']
        self.tiles['m1']['adjacency_members'] = ['o1','o2','m2','i1','i0','m0']
        self.tiles['m2']['adjacency_members'] = ['o2','o3','o4','m3','i1','m1']
        self.tiles['m3']['adjacency_members'] = ['m2','o4','o5','m4','i2','i1']
        self.tiles['m4']['adjacency_members'] = ['m3','o5','o6','o7','m5','i2']
        self.tiles['m5']['adjacency_members'] = ['i2','m4','o7','o8','m6','i3']
        self.tiles['m6']['adjacency_members'] = ['i3','m5','o8','o9','o10','m7']
        self.tiles['m7']['adjacency_members'] = ['i4','i3','m6','o10','o11','m8']
        self.tiles['m8']['adjacency_members'] = ['m9','i4','m7','o11','o12','o13']
        self.tiles['m9']['adjacency_members'] = ['m10','i5','i4','m8','o13','o14']
        self.tiles['m10']['adjacency_members'] = ['o16','m11','i5','m9','o14','o15']
        self.tiles['m11']['adjacency_members'] = ['o17','m0','i0','i5','m10','o16']
        self.tiles['o0']['adjacency_members'] = ['','','i1','m0','o17','']
        self.tiles['o1']['adjacency_members'] = ['','','o2','m1','m0','o0']
        self.tiles['o2']['adjacency_members'] = ['','','o3','m2','m1','o1']
        self.tiles['o3']['adjacency_members'] = ['','','','o4','m2','o2']
        self.tiles['o4']['adjacency_members'] = ['o3','','','o5','m3','m2']
        self.tiles['o5']['adjacency_members'] = ['o4','','','o6','m4','m3']
        self.tiles['o6']['adjacency_members'] = ['o5','','','','o7','m4']
        self.tiles['o7']['adjacency_members'] = ['m4','o6','','','o8','m5']
        self.tiles['o8']['adjacency_members'] = ['m5','o7','','','o9','m6']
        self.tiles['o9']['adjacency_members'] = ['m6','o8','','','','o10']
        self.tiles['o10']['adjacency_members'] = ['m7','m6','o9','','','o11']
        self.tiles['o11']['adjacency_members'] = ['m8','m7','o10','','','o12']
        self.tiles['o12']['adjacency_members'] = ['o13','m8','o11','','','']
        self.tiles['o13']['adjacency_members'] = ['o14','m9','m8','o12','','']
        self.tiles['o14']['adjacency_members'] = ['o15','m10','m9','o13','','']
        self.tiles['o15']['adjacency_members'] = ['','o16','m10','o14','','']
        self.tiles['o16']['adjacency_members'] = ['','o17','m11','m10','o15','']
        self.tiles['o17']['adjacency_members'] = ['','o0','m0','m11','o16','']

        self.game['erah'] = 8 # Temp set to 8
        self.game['strategic'] = None
        self.game['luxury'] = None

        self.city['govener'] = None
        self.city['population'] = None
        self.city['houseing'] = None
        self.city['food'] = None
        self.city['production'] = None
        self.city['gold'] = None
        self.city['science'] = None
        self.city['culture'] = None
        self.city['faith'] = None
        self.city['power'] = None
        self.city['amenities'] = None
        self.city['trader'] = False



    def print_grid(self):

        print('City center')
        print(' cc ')

        print('Inner ring')
        print('  5 0  ')
        print('4     1')
        print('  3 2  ')

        print('Middle ring')
        print('        10   11   0        ')
        print('     9               1     ')
        print(' 8                       2 ')
        print('     7               3     ')
        print('         6   5   4         ')

        print('Outer ring')
        print('              15  16  17   0              ')
        print('          14                   1          ')
        print('      13                           2      ')
        print('  12                                   3  ')
        print('      11                           4      ')
        print('          10                   5          ')
        print('               9   8   7   6              ')

    def itterate_through_selections(self):
        for k,v in self.tiles.items():
            print('\n')
            print('grassland: g | tundra: t | lake: l  ')
            print('plains: p    | snow: s   | ocean: o ')
            print('desert: d    | coast: c  |          ')
            print(f"Select the Terrain for: {k} (remember add 'h' for hills, and <enter> for none)")
            self.tiles[k]['terrain'] = input('')

            print('')

            print('woods: 1       | mountains: 7 | volcano: 12       ')
            print('rainforest: 2  | cliffs: 8    | volcanic_soil: 13 ')
            print('marsh: 3       | reef: 9      | geothermal: 14    ')
            print('river: 4       | ice: 10      |                   ')
            print('floodplains: 5 | cataract: 11 |                   ')
            print('oasis: 6       |                                  ')
            print(f"Select the Feature for: {k}")
            self.tiles[k]['feature'] = input('')
            # print(f"Is there more there?: {k}")

    def return_terrain(self, character):
        terrain_object = terrain.Terrain()
        if character == 'g':
            terrain_object.grassland()

        elif character == 'gh':
            terrain_object.grasslandh()

        elif character == 'p':
            terrain_object.plains()

        elif character == 'ph':
            terrain_object.plainsh()

        elif character == 'd':
            terrain_object.desert()

        elif character == 'dh':
            terrain_object.deserth()

        elif character == 't':
            terrain_object.tundra()

        elif character == 'th':
            terrain_object.tundrah()

        elif character == 's':
            terrain_object.snow()

        elif character == 'sh':
            terrain_object.snowh()

        elif character == 'c':
            terrain_object.coast()

        elif character == 'l':
            terrain_object.lake()

        elif character == 'o':
            terrain_object.ocean()

        else:
            terrain_object.none()

        return terrain_object


    def return_feature(self, number):
        feature_object = feature.Feature()
        if number in [1, '1']:
            feature_object.woods()

        elif number in [2, '2']:
            feature_object.rainforest()

        elif number in [3, '3']:
            feature_object.marsh()

        elif number in [4, '4']:
            feature_object.floodplains()

        elif number in [5, '5']:
            feature_object.oasis()

        elif number in [6, '6']:
            feature_object.mountains()

        elif number in [7, '7']:
            feature_object.cliffs()

        elif number in [8, '8']:
            feature_object.reef()

        elif number in [9, '9']:
            feature_object.ice()

        elif number in [10, '10']:
            feature_object.cataract()

        elif number in [11, '11']:
            feature_object.volcano()

        elif number in [12, '12']:
            feature_object.volcanic_soil()

        elif number in [13, '13']:
            feature_object.geothermal()

        else:
            feature_object.none()

        return feature_object


    def return_river(self, number):
        # feature_object = feature.Feature()
        try:
            if int(number) > 0:
                return int(number)
            elif int(number) == 0:
                return 0
        except ValueError:
            return 0

    def return_natural_wonder(self, wonder_string):
        pass
    def return_district(self, character):
        return 'set'
    def return_improvement(self, character):
        pass
    def return_wonder(self, wonder_string):
        pass

    def calculate_adjacency(self, tile):
        # print(tile)
        for adj in tile['adjacency_members']:
            if adj == '':
                continue
            # print(adj)
            # print(self.tiles[adj])
            # print(tile['terrain'].terrain, self.tiles[adj]['terrain'].terrain)

    def csv_selection(self, terrains=None, features=None, rivers=None, districts=None, improvements=None):
        tile_keys = self.tiles.keys()
        if terrains == None:
            print('\n')
            print('grassland: g | tundra: t | lake: l  ')
            print('plains: p    | snow: s   | ocean: o ')
            print('desert: d    | coast: c  |          ')
            print(f"Select the Terrain separated by camas: (remember add 'h' for hills, and 0 or '' for none, there should be 39)")
            # print('cc,i0,i1,i2,i3,i4,i5,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17')
            print('c,i,i,i,i,i,i,m,m,m,m,m,m,m,m,m,m,m,m,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o')
            terrains = input('')

        terrains = terrains.split(',')
        for index, key in enumerate(self.tiles.keys()):
            self.tiles[key]['terrain'] = self.return_terrain(terrains[index])

        print('')

        if features == None:
            print('woods: 1       | mountains: 6 | volcano: 11       ')
            print('rainforest: 2  | cliffs: 7    | volcanic_soil: 12 ')
            print('marsh: 3       | reef: 8      | geothermal: 13    ')
            print('floodplains: 4 | ice: 9       |                   ')
            print('oasis: 5       | cataract: 10 |                   ')
            print(f"Select the Feature separated by camas: (0 or '' for none, there should be 39")
            print('c,i,i,i,i,i,i,m,m,m,m,m,m,m,m,m,m,m,m,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o')
            # print('cc,i0,i1,i2,i3,i4,i5,m0,m1,m2,m3,m4,m5,m6,m7,m8,m9,m10,m11,o0,o1,o2,o3,o4,o5,o6,o7,o8,o9,o10,o11,o12,o13,o14,o15,o16,o17')
            features =  input('')

        features = features.split(',')
        for index, key in enumerate(self.tiles.keys()):
            self.tiles[key]['feature'] = self.return_feature(features[index])

        print('')

        if rivers == None:
            print('River next to tile?')
            print(f"Select the Terrain separated by camas: (remember add 'h' for hills, and 0 or '' for none, there should be 39)")
            print('c,i,i,i,i,i,i,m,m,m,m,m,m,m,m,m,m,m,m,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o,o')
            rivers = input('')

        rivers = rivers.split(',')
        for index, key in enumerate(self.tiles.keys()):
            self.tiles[key]['river'] = self.return_river(rivers[index])

        print('')

        if districts == None:
            print('set up district input')
        
        districts = districts.split(',')
        for index, key in enumerate(self.tiles.keys()):
            self.tiles[key]['district'] = self.return_district(districts[index])

    def calculate_food_basket(self, current_pop):
        n = current_pop
        food_basket = (n ** 1.5) + (8 * n) + 15
        return food_basket

    def calculate_tile_yield(self, tile):


        if self.city['food'] == None:
            self.city['food'] = 0

        if self.city['production'] == None:
            self.city['production'] = 0

        if self.city['gold'] == None:
            self.city['gold'] = 0

        if self.city['science'] == None:
            self.city['science'] = 0

        if self.city['culture'] == None:
            self.city['culture'] = 0

        if self.city['faith'] == None:
            self.city['faith'] = 0


        print(tile)
        self.city['food'] += sum([
            tile['terrain'].food,
            tile['feature'].food,
        ])
        self.city['production'] += sum([
            tile['terrain'].production,
            tile['feature'].production,
        ])
        self.city['gold'] += sum([
            tile['terrain'].gold,
            tile['feature'].gold,
        ])
        # print(self.city['food'], self.city['production'], self.city['gold'])
        # print(self.city)
        # print(tile['terrain'].food, tile['terrain'].production, tile['terrain'].gold)
        # print(tile['feature'].food, tile['feature'].production, tile['feature'].gold)
        # print(tile['natural_wonders'].food, tile['natural_wonders'].production, tile['natural_wonders'].gold)
        # print(tile['improvements'].food, tile['improvements'].production, tile['improvements'].gold)
        # print(tile['districts'].food, tile['districts'].production, tile['districts'].gold)
        # print(tile['wonders'].food, tile['wonders'].production, tile['wonders'].gold)
        # print(tile['adjacency'].food, tile['adjacency'].production, tile['adjacency'].gold)



    def calculate_yields(self):
        for index, key in enumerate(self.tiles.keys()):
            # print(self.tiles[key])
            self.calculate_tile_yield(self.tiles[key])
            # self.calculate_adjacency(self.tiles[key])
            # print(self.tiles[key])
            # print(self.tiles[key]['terrain'].food, self.tiles[key]['terrain'].production, self.tiles[key]['terrain'].gold)
            # print(self.tiles[key]['feature'].food, self.tiles[key]['feature'].production, self.tiles[key]['feature'].gold, self.tiles[key]['feature'].science)
            # print(self.tiles[key]['river'])
            # print(type(self.tiles[key]['terrain'].terrain))
            # print(self.tiles[key]['terrain'].terrain)


    def print_tiles(self):
        for k,v in self.tiles.items():
            print(k,v)









cv = CivVI()
# cv.print_grid()
# cv.itterate_through_selections()
cv.csv_selection('g,g,d,p,p,g,0,g,d,d,p,p,p,p,p,g,0,0,0,g,d,d,c,c,c,c,p,p,p,p,p,g,g,g,g,g,g',
                 '1,1,0,0,0,1,6,1,0,0,0,0,0,0,0,1,6,6,6,1,,,,,,,,,,,,1,1,1,1,1,1',
                 '1,1,1,1,0,0,1,,,1,1,,,,,,,,,,,,1,1,,,,,,,,,,,,,',
                 'City Center,Campus,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,',)
# cv.csv_selection()
cv.calculate_yields()
# print(cv.tiles['cc']['terrain'], cv.tiles['i0']['terrain'])
# print(cv.tiles['cc']['terrain'].terrain, cv.tiles['i0']['terrain'].terrain)
# ter = terrain.Terrain()
# print(ter.adjacencie_check(cv.tiles['cc']['terrain'], cv.tiles['i0']['terrain']))
# print(ter.adjacencie_check(cv.tiles['cc']['terrain'], cv.tiles['i1']['terrain']))
# print(cv.tiles['cc'])


# cv.print_tiles()self.tiles