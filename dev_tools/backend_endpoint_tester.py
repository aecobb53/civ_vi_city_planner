import requests
import json

port = '8314'
url = 'http://0.0.0.0:' + port

print(f"url: {url}")
print('verifying heartbeat')
try:
    r = requests.get(url)
except:
    port = '8204'
    url = 'http://0.0.0.0:' + port
    r = requests.get(url)
print(r)
print(r.text)

# # exit()
# print('')

# post_data = {
#     "name": "Foo",
#     "description": "An optional description",
#     "price": 45.2,
#     "tax": 3.5
# }
# item_url = url + '/items/'
# print(f"url: {item_url}")
# print('running item class')
# r = requests.post(item_url, data=json.dumps(post_data))
# print(r)
# print(r.text)

# # exit()
# print('')

# post_data = {
#     'name':'somename',
#     'testvar':'something else',
#     'ignorevar':'this is ignored because its not set',
#     'center':[],
#     'inner':[],
#     'middle':[],
#     'outer':[],
#     'nearby':[],
# }
# null_city_url = url + '/city_plan/'
# print(f"url: {null_city_url}")
# print('running null item class')
# r = requests.post(null_city_url, data=json.dumps(post_data))
# print(r)
# print(r.text)
# try:
#     print(json.dumps(r.json, indent=4))
# except:
#     print('not json parsable')

# exit()
print('')


post_data = {
    'center':[
        {
            'terrain':{
                'name': 'grassland',
                'hills': True,
            },
            'feature':{
                'name':'woods',
                'river': True,
            },
            'resource':{
                'name':'iron',
            },
            'improvement':{
                'name':'farm'
            },
            'district':{
                'name':'campus'
            },
        },
        # {
        #     'terrain':{
        #         'name': 'desert',
        #         'hills':True,
        #     },
        #     'feature':{
        #         'name':'floodplains',
        #         'river':True,
        #     },
        # },
        # {
        #     'terrain':{
        #         'name': 'plains',
        #         'hills':False,
        #     },
        #     'feature':{
        #         'name':'rainforest',
        #         'river':False,
        #     },
        # },
        # {},
        # {},
        # {},
    ],
    'inner':[
        {
            'terrain':{
                'name': 'grassland',
            },
            'feature':{
                'name':'woods',
            },
            'resource':{
                'name':'iron',
            },
            'improvement':{
                'name':'farm'
            },
            'district':{
                'name':'campus'
            },
        },
        {
            'terrain':{
                'name': 'desert',
                'hills':True,
            },
            'feature':{
                'name':'floodplains',
                'river':True,
            },
        },
        {
            'terrain':{
                'name': 'plains',
                'hills':True,
            },
            'feature':{
                'name':'rainforest',
                'river':False,
            },
        },
        {},
        {},
        {},
    ],
    'middle':[],
    'outer':[],
    'nearby':[],
}
city_url = url + '/city_plan/'
print(f"url: {city_url}")
# print('running null item class')
r = requests.post(city_url, data=json.dumps(post_data))
print(r)
print(r.text)
if r.status_code != 200:
    raise ValueError('the code is wrong yo')
try:
    rj = r.json()
    print(json.dumps(rj, indent=4))
    city_id = rj['cityId']
except:
    print('not json parsable')
    exit()

# exit()
print('')

post_data = {
    'cityId':city_id,
}
city_url = url + '/city_plan/'
print(f"url: {city_url}")
# print('running null item class')
r = requests.get(city_url, data=json.dumps(post_data))
print(r)
print(r.text)
if r.status_code != 200:
    raise ValueError('the code is wrong yo')
try:
    print(json.dumps(r.json(), indent=4))
except:
    print('not json parsable')
