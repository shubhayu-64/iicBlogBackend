# import statements
from pymongo import MongoClient
from models.models import articleDbModel, articleRequestModel, articleResponseModel, miniArticleModel
from datetime import date
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

# create db connection
connection = MongoClient(os.getenv("mongoCred"))
database = connection[os.getenv("database")]
collection = database[os.getenv("collection")]


async def getAllArticles(limit, offset):
    data = list(collection.find({}).skip(offset).limit(limit))
    articles = []
    for entry in data:
        entry["body"] = entry["body"][0].partition('.')[0] + "."
        entry["tags"] = entry["tags"][0]
        articles.append(miniArticleModel(**entry))
    return articles


async def getTagArticles(tagName, limit, offset):
    data = list(collection.find({"tags.0": tagName}).skip(offset).limit(limit))
    articles = []
    for entry in data:
        entry["body"] = entry["body"][0].partition('.')[0] + "."
        entry["tags"] = entry["tags"][0]
        articles.append(miniArticleModel(**entry))
    return articles


async def getUserArticles(username, limit, offset):
    data = list(collection.find(
        {"username": username}).skip(offset).limit(limit))
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


async def getArticleCount(username: str):
    return len(list(collection.find({"username": username})))


async def createArticle(article: articleRequestModel):
    articleData = article.copy()
    articleData = articleData.dict()
    dbData = {
        "articleId": hashlib.md5((articleData["username"] + str(getArticleCount(articleData["username"]))).encode("utf-8")).hexdigest(),
        "postedDate": date.today().strftime("%B %d, %Y"),
        "likes": 0,
    }
    articleData.update(dbData)
    article = articleDbModel(**articleData)
    collection.insert_one(dict(article))
