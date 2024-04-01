import pymongo
CONNECTIONSTRING="mongodb+srv://jerryhash231:4ZtcY6TjwfpgIYcR@cluster0.zoxlymw.mongodb.net/"
myclient = pymongo.MongoClient(CONNECTIONSTRING)
db =myclient['parmar']
collection = db["coll"]
h = {
    "jenil":"parmar",
    "age":198
}
collection.insert_one(h)