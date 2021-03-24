
from pymongo import MongoClient, errors

domain = '172.24.0.2'
mongoport1 = 27017

# pprint library is used to make the output look more pretty
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(str(domain) + ':' + str(mongoport1))
db=client.admin
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
print(serverStatusResult)

# # client = MongoClient(
# #     host = [ str(domain) + ':' + str(mongoport1) ],
# #     serverSelectionTimeoutMS = 3000,
# #     username = 'objectrocket',
# #     password = '1234'
# # )

# # print ("server version:", client.server_info()["version"])

# # database_names = client.list_database_names()

# # use a try-except indentation to catch MongoClient() errors
# try:
#     # try to instantiate a client instance
#     client = MongoClient(
#         host = [ str(domain) + ":" + str(mongoport1) ],
#         serverSelectionTimeoutMS = 3000, # 3 second timeout
#         username = "root",
#         password = "rootpassword",
#     )

#     # print the version of MongoDB server if connection successful
#     print ("server version:", client.server_info()["version"])

#     # get the database_names from the MongoClient()
#     database_names = client.list_database_names()

# except errors.ServerSelectionTimeoutError as err:
#     # set the client and DB name list to 'None' and `[]` if exception
#     client = None
#     database_names = []

#     # catch pymongo.errors.ServerSelectionTimeoutError
#     print ("pymongo ERROR:", err)

# print ("\ndatabases:", database_names)

# client = MongoClient(
#     host = [ str(domain) + ":" + str(mongoport1) ],
#     serverSelectionTimeoutMS = 3000, # 3 second timeout
#     username = "root",
#     password = "rootpassword",
# )
# print(client)
# db=client.admin
# serverStatusResult=db.command("serverStatus")
# print(serverStatusResult)
