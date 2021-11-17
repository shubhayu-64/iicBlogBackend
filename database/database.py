#import statements
from pymongo import MongoClient
from models.models import articleDbModel, articleRequestModel, articleResponseModel, miniArticleModel
from datetime import date
from dotenv import load_dotenv

load_dotenv()

# create db connection
connection = MongoClient(
    "mongodb+srv://admin:IICblog_admin@iicblogdb.fidhh.mongodb.net/myFirstDatabase?authSource=admin&replicaSet=atlas-un1fbw-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true")

database = connection.iicblog
collection = database.articles


async def getAllArticles():
    data = list(collection.find({}))
    articles = []
    for entry in data:
        entry["body"] = entry["body"][0].partition('.')[0] + "."
        entry["tags"] = entry["tags"][0]
        articles.append(miniArticleModel(**entry))
    return articles


async def fetch_one_article(article_id):
    document = collection.find_one({"article_id": article_id})
    return document


async def getArticle(username: str, articleId: str):
    articleData = collection.find_one(
        {"username": username, "articleId": articleId})
    articleData = articleResponseModel(**articleData)
    return articleData


async def createArticle(article: articleRequestModel):
    articleData = article.copy()
    articleData = articleData.dict()
    dbData = {
        "username": "admin",
        "articleId": str(len(articleData)),
        "author": "Shubhayu Majumdar",
        "postedDate": date.today().strftime("%B %d, %Y"),
        "likes": 0,
    }
    articleData.update(dbData)
    article = articleDbModel(**articleData)
    collection.insert_one(dict(article))
