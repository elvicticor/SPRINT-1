from pymongo import MongoClient

mongodb_url = "mongodb+srv://victornieto:victor0621@cluster0.8eg5mmb.mongodb.net/?retryWrites=true&w=majority"
port = 8000

conn = MongoClient(mongodb_url, port)
db = conn["tiendaOnline"]