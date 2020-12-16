import shutil

exit()

path_to_reference = 'backend/resources/bananas.py'

new_directory = 'backend/resources/'

list_of_names = [
    'copper',
    'cattle',
    'crabs',
    'deer',
    'fish',
    'maize',
    'rice',
    'sheep',
    'stone',
    'wheat',
    'amber',
    'cinnamon',
    'citrus',
    'cloves',
    'cocoa',
    'coffee',
    'cosmetics',
    'cotton',
    'dyes',
    'diamonds',
    'furs',
    'gold_ore',
    'gypsum',
    'honey',
    'insense',
    'ivory',
    'jade',
    'jeans',
    'marble',
    'murcury',
    'olives',
    'pearls',
    'perfume',
    'salt',
    'silk',
    'silver',
    'spices',
    'sugar',
    'tea',
    'tobacco',
    'toys',
    'truffles',
    'turtles',
    'whales',
    'wine',
    'horses',
    'iron',
    'niter',
    'coal',
    'oil',
    'aluminum',
    'uranium',
]

for line in list_of_names:
    filename = new_directory + line + '.py'
    print(filename)
    shutil.copy(path_to_reference, filename)