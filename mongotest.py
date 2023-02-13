import pymongo
client = pymongo.MongoClient("mongodb+srv://balraj:mehra2012@cluster0.fqzcer7.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d={"name":"balraj","surname":"mehra","emailid":"balrajmehra2012"}
db1=client["mongodb"]
call=db1["test"]
call.insert_one(d)