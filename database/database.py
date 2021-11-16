#import statements
from pymongo import MongoClient
from models.articles import article
from dotenv import load_dotenv

load_dotenv()

#create db connection
connection = MongoClient("mongodb+srv://admin:IICblog_admin@iicblogdb.fidhh.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-un1fbw-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")

database = connection.iicblog
collection = database.articles

async def fetch_all_articles():
    articles = []
    cursor = collection.find({})
    for document in cursor:
        articles.append(article(**document))
    return articles

async def fetch_one_article(article_id):
    document = await collection.find_one({"article_id": article_id})
    return document

