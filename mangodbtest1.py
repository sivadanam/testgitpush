import pymongo
client = pymongo.MongoClient("mongodb+srv://lucky:Lucky_1002@cluster1002.rgr95.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={
   "name": "lucky",
    "email":"anusha.sivadanam1002@gmail.com",
    "surname":"babu"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)