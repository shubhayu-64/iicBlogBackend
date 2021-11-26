#import statements
from fastapi import FastAPI
from routes.routes import articleRouter
from fastapi.middleware.cors import CORSMiddleware

apiDescription = """
## IIC Blog Backend
### Version: 0.1.0
"""

app = FastAPI(title="IIC Blog", description=apiDescription, contact={
              "name": "IIC Techno Main Saltlake", "url": "https://iictmsl.in/"})

origins = [
    "http://localhost:3000", "https://iicblog.netlify.app"
]

# what is a middleware?
# software that acts as a bridge between an operating system or database and applications, especially on a network.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# register router
app.include_router(articleRouter)
