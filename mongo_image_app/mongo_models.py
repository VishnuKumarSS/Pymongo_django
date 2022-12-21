import pymongo 
import gridfs
from django.conf import settings


try:
    client = pymongo.MongoClient() # empty means localhost with mongodb default port 27017 # or we can pass MongoClient("127.0.0.1", "27017")
except Exception:
    print("Error: ", Exception)

my_db = client[settings.MONGO_DB_NAME]

my_collection = my_db[settings.MONGO_COLLECTION_NAME]

# file system
fs = gridfs.GridFS(my_db)
