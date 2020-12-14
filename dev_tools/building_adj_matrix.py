dct = {
    'cc': ['i0','i1','i2','i3','i4','i5'],
    'i0': ['m0','m1','i1','cc','i5','m11'],
    'i1': ['m1','m2','m3','i2','cc','i0'],
    'i2': ['i1','m3','m4','m5','i3','cc'],
    'i3': ['cc','i2','m5','m6','m7','i4'],
    'i4': ['i5','cc','i3','m7','m8','m9'],
    'i5': ['m11','i0','cc','i4','m9','m10'],
    'm0': ['o0','o1','m1','i0','m11','o17'],
    'm1': ['o1','o2','m2','i1','i0','m0'],
    'm2': ['o2','o3','o4','m3','i1','m1'],
    'm3': ['m2','o4','o5','m4','i2','i1'],
    'm4': ['m3','o5','o6','o7','m5','i2'],
    'm5': ['i2','m4','o7','o8','m6','i3'],
    'm6': ['i3','m5','o8','o9','o10','m7'],
    'm7': ['i4','i3','m6','o10','o11','m8'],
    'm8': ['m9','i4','m7','o11','o12','o13'],
    'm9': ['m10','i5','i4','m8','o13','o14'],
    'm10': ['o16','m11','i5','m9','o14','o15'],
    'm11': ['o17','m0','i0','i5','m10','o16'],
    'o0': ['','','i1','m0','o17',''],
    'o1': ['','','o2','m1','m0','o0'],
    'o2': ['','','o3','m2','m1','o1'],
    'o3': ['','','','o4','m2','o2'],
    'o4': ['o3','','','o5','m3','m2'],
    'o5': ['o4','','','o6','m4','m3'],
    'o6': ['o5','','','','o7','m4'],
    'o7': ['m4','o6','','','o8','m5'],
    'o8': ['m5','o7','','','o9','m6'],
    'o9': ['m6','o8','','','','o10'],
    'o10': ['m7','m6','o9','','','o11'],
    'o11': ['m8','m7','o10','','','o12'],
    'o12': ['o13','m8','o11','','',''],
    'o13': ['o14','m9','m8','o12','',''],
    'o14': ['o15','m10','m9','o13','',''],
    'o15': ['','o16','m10','o14','',''],
    'o16': ['','o17','m11','m10','o15',''],
    'o17': ['','o0','m0','m11','o16',''],
}

for k, v in dct.items():
    nl = []
    for i in v:
        if i == '':
            nl.append('None')
        else:
            nl.append('self.' + i)
    print(f"'{k}': [{', '.join(nl)}],")