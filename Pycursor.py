python3

from pymongo import MongoClient
client = MongoClient('mongodb://wavelet:27017/')
1,2,3,4,5,6
with client:
    
    db = client.carsdb

    cars = db.cars.find()

    print(cars.next())
    print(cars.next())
    print(cars.next())
    
    cars.rewind()

    print(cars.next())
    print(cars.next())
    print(cars.next())    

    print(list(cars))







