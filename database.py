from pymongo import MongoClient
import config

conn = MongoClient(config.mongodb_uri, config.port)