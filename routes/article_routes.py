#import statements
from fastapi import APIRouter, HTTPException
from models.articles import article
from config.database import collection, fetch_all_articles, fetch_one_article
from schemas.article_sc import articleEntity

article_router = APIRouter()

@article_router.get('/hello_world')
async def hello_world():
    return "hello world"

    
@article_router.get("/api/article")
async def all_articles():
    response = await fetch_all_articles()
    return response

@article_router.get("/api/article/{article_id}", response_model= article)
async def get_article(article_id):
    response = fetch_one_article(article_id)
    if response:
        return response
    raise HTTPException(404, f"There is no article with this id -> {article_id}")


@article_router.post('/article')
async def create_article(article: article):
    collection.insert_one(dict(article))
    return "Successfully created"
    