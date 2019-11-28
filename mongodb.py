from pymongo import MongoClient
from bson.objectid import ObjectId

conn = MongoClient("2.2.2.200", 27017)

db = conn.mydb

collection = db.student
collection.insert_one({'name': 'jerry', 'age': 10.0, 'gender': 1, 'address': '上海', 'isdelete': 0.0})
data = collection.find()
for i in data:
    print(i)
print(collection.count_documents({'age': {'$gt': 10}}))
print(collection.count_documents({}))
print(collection.find_one({"_id": ObjectId("5dde61e4eeda653e01ba5401")}))
collection.update_one({"age": 10},{"$set": {"age": 12}})
collection.delete_one({"age": 10})
print(collection.find_one())
conn.close()
