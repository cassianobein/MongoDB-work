python3

from pymongo import MongoClient
printm1
client = MongoClient('mongodb://localhost:27017/')

with client:    
    db = client.testdb
    print(db.collection_names())
    
    
