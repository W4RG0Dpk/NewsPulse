from pymongo import MongoClient
from config.settings import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)

db = client[DB_NAME]

raw_articles = db["raw_articles"]

scrape_logs = db["scrape_logs"]