python3
print 1,2,3,4,5,6,7,
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

with client:    
    db = client.testdb
    print(db.collection_names())
    
    
