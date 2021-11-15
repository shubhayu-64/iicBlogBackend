#import statements
from pydantic import BaseModel

class article(BaseModel):
    article_id: str
    title: str
    tags: str
    author_name: str
    date_time: str
    content: str
    img_url: str
    likes: str
