from pymongo import MongoClient
from datetime import datetime
import certifi

file = open("dbCredentials", "r")
credentials = file.readline()
file.close()




cluster = f"mongodb+srv://{credentials}@cluster0.5cggy.mongodb.net/test?retryWrites=true&w=majority"
newclient = MongoClient(cluster, tlsCAFile=certifi.where())
db = newclient.test
passwords = db.passwords
print("works")

def addPassword():
    password1 = {
    "website":"www.example.com",
     "password":"123456",
     "date":datetime.now().strftime("%d/%m/%Y %H:%M:%S")



}
    passwords.insert_one(password1)