# Importing FastAPI
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI()

# Define a route
@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "About page"}

class Blog(BaseModel):
    title: str 
    body: str
    published: Optional[bool]


@app.get("/blog")
def blog(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"message": f"{limit} published blogs from the db"}
    return {"message": f"{limit} blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {"message": "Unpublished blogs"}

@app.get("/blog/{id}")
def blog(id: int):
    return {"message": f"Blog page {id}"}


@app.post("/blog")
def create_blog(blog: Blog):
    return {"message": f"Blog created successfully with title {blog.title}"}

