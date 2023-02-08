from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_DB = os.getenv('MONGO_DB')

client = MongoClient(MONGO_HOST)

try:
    conn = client.server_info()
    print("Connected to MongoDB")
except:
    print("Unable to connect MongoDB")

client.get_database(MONGO_DB).get_collection("rooms").insert_many([{
    "id": i,
    "brightness_level": 127,
    "state": 0,
    "mode": 0
} for i in range(1, 4)])
