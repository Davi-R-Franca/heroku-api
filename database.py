from pymongo import MongoClient
import config

conn = MongoClient(config.mongodb_uri, config.port)
mydb = conn['teste']
mycol = mydb['teste-1']