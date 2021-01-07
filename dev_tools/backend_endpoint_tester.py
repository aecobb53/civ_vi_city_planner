import requests
import json

port = '8314'
url = 'http://0.0.0.0:' + port

print(f"url: {url}")
print('verifying heartbeat')
r = requests.get(url)
print(r)
print(r.text)

# exit()
print('')

post_data = {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
item_url = url + '/items/'
print(f"url: {item_url}")
print('running item class')
r = requests.post(item_url, data=json.dumps(post_data))
print(r)
print(r.text)

# exit()
print('')

post_data = {
    'name': "alberta",
    'center': "center ring",
    'inner': "inner ring",
    'middle': "middle ring",
    'outer': "outer ring",
    'nearby': "nearby ring",
}
post_data = {
    # 'name': "alberta",
    'center': [
        "center ring",
    ],
    'inner': [
        "inner ring",
    ],
    'middle': [
        "middle ring",
    ],
    'outer': [
        "outer ring",
    ],
    'nearby': [
        "nearby ring",
    ],
}
city_url = url + '/city_plan/'
print(f"url: {city_url}")
print('running item class')
r = requests.post(city_url, data=json.dumps(post_data))
print(r)
print(r.text)
try:
    print(json.dumps(r.json, indent=4))
except:
    print('not json parsable')
