import pymongo

# docker run -d -p 27017:27017 --name m1 mongo

host = 'localhost'
host = 'civ_vi_city_planner_database_1'
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient = pymongo.MongoClient("mongodb://civ_vi_city_planner_database_1:27017/")
myclient = pymongo.MongoClient(f"mongodb://{host}:27017/")

mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "name": "Amy", "address": "Apple st"},
  { "name": "Am2", "address": "Apple st2"},
  { "name": "Am3", "address": "Apple st3"}
]

# x = mycol.insert_many(mylist)

# print(x.inserted_ids)

for x in mycol.find():
  print(x)
