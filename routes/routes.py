#import statements
from fastapi import APIRouter, HTTPException, exceptions, status
from fastapi.responses import RedirectResponse
from models.models import *
from typing import List, Optional
from database.database import createArticle, getAllArticles, getArticle, getTagArticles, getUserArticles


# App declaration
articleRouter = APIRouter()


@articleRouter.get("/")
async def root():
    '''
    Redirects users to Documentation page.
    '''
    return RedirectResponse("/docs")


@articleRouter.get("/@{username}", response_model=List[miniArticleModel])
async def get_user_articles(username: str, limit: Optional[int] = 20, offset: Optional[int] = 0):
    '''
    Gets articles for homepage. 
    Returns a mini article format for listing.
    '''
    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="My database dumped me bro. (╥_╥)")
    try:
        allArticles = await getUserArticles(username, limit, offset)
        if not allArticles:
            raise exception
        return allArticles
    except:
        raise exception


@articleRouter.get("/home/articles", response_model=List[miniArticleModel])
async def get_homepage_articles(limit: Optional[int] = 20, offset: Optional[int] = 0):
    '''
    Gets articles for homepage. 
    Returns a mini article format for listing.
    '''
    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="My database dumped me bro. (╥_╥)")
    try:
        allArticles = await getAllArticles(limit, offset)
        if not allArticles:
            raise exception
        return allArticles
    except:
        raise exception


@articleRouter.get("/tag/{tagName}", response_model=List[miniArticleModel])
async def get_tag_articles(tagName: str, limit: Optional[int] = 20, offset: Optional[int] = 0):
    '''
    Gets articles for homepage. 
    Returns a mini article format for listing.
    '''
    exception = HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail="My database dumped me bro. (╥_╥)")
    try:
        allArticles = await getTagArticles(tagName, limit, offset)
        if not allArticles:
            raise exception
        return allArticles
    except:
        raise exception


@articleRouter.get("/@{username}/{article}", response_model=articleResponseModel)
async def get_article(username: str, article: str):
    '''
    Gets article for specific username and article ID.
    Returns all details of article.
    '''
    exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail="Didn't find your article. You noob!")
    try:
        articleData = await getArticle(username, article)
        if not articleData:
            raise exception
        return articleData
    except:
        raise exception


@articleRouter.post('/article')
async def create_article(article: articleRequestModel):
    '''
    Stores the article in databse
    Returns success state.
    '''
    try:
        await createArticle(article)
        return {"success": True}
    except:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                            detail="Article did not process. You noob!")
