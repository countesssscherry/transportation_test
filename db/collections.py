from config import DB_CONNECTION
import pymongo

cursor = pymongo.MongoClient(DB_CONNECTION)
db = cursor.transport

transportations = db['transportations']