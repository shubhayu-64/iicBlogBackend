#import statements
from typing import List
from pydantic import BaseModel, Field
from pydantic.networks import HttpUrl


class comments(BaseModel):
    username: str = Field(...)
    body: str = Field(...)
    postedDate: str = Field(...)
    likes: int = Field(...)
    author: str = Field(...)


class miniArticleModel(BaseModel):
    username: str = Field(...)
    articleId: str = Field(...)
    author: str = Field(...)
    title: str = Field(...)
    body: str = Field(...)
    imageUrl: HttpUrl = Field(...)
    postedDate: str = Field(...)
    tags: str = Field(...)


class articleResponseModel(BaseModel):
    username: str = Field(...)
    articleId: str = Field(...)
    author: str = Field(...)
    title: str = Field(...)
    body: List[str] = Field(default_factory=list, min_items=1)
    imageUrl: HttpUrl = Field(...)
    postedDate: str = Field(...)
    likes: int = Field(...)
    tags: List[str] = Field(default_factory=list, min_items=1, max_items=3)
    commentThread: List[comments] = Field(default_factory=list)
    similarArticles: List[miniArticleModel] = Field(
        default_factory=list, max_items=6)


class articleRequestModel(BaseModel):
    title: str = Field(...)
    body: List[str] = Field(default_factory=list, min_items=1)
    imageUrl: HttpUrl = Field(...)
    tags: List[str] = Field(default_factory=list, min_items=1, max_items=3)


class articleDbModel(BaseModel):
    username: str = Field(...)
    articleId: str = Field(...)
    author: str = Field(...)
    title: str = Field(...)
    body: List[str] = Field(default_factory=list, min_items=1)
    imageUrl: HttpUrl = Field(...)
    postedDate: str = Field(...)
    likes: int = Field(...)
    tags: List[str] = Field(default_factory=list, min_items=1, max_items=3)
    commentThread: List[comments] = Field(default_factory=list)
    similarArticles: List[miniArticleModel] = Field(
        default_factory=list, max_items=6)
