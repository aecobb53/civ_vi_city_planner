import requests
import json

port = '8314'
port = '8000'
url = 'http://0.0.0.0:' + port

print(f"url: {url}")
r = requests.get(url)
print(r)
print(r.text)

exit()

post_data = {
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}

# post_data = {
#     'name',
#     'center',
#     'inner',
#     'middle',
#     'outer',
#     'nearby',
# }

url += '/items/'

print(f"url: {url}")
r = requests.post(url, data=json.dumps(post_data))
print(r)
print(r.text)
