from fastapi import FastAPI,Depends,status,Response,HTTPException
from blog import models
from blog.schemas import Blog
from blog.database import engine,SessionLocal
from sqlalchemy.orm import Session



app = FastAPI()

models.Base.metadata.create_all(bind=engine)



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(blog: Blog, db: Session = Depends(get_db)):
    new_model = models.Blog(title=blog.title, body=blog.body)
    db.add(new_model)
    db.commit()
    db.refresh(new_model)
    return new_model

@app.get("/blog")
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}",status_code=status.HTTP_200_OK)
def get_blog(id: int,response: Response,db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=
            f"No Blog Available with id {id}"
        )
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"detail":f"No Blog Available with id {id}"}
    return blog


@app.delete("/blog/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return None

@app.put('/blog/{id}')
def update_blog(id: int,blog: Blog,response: Response, db: Session = Depends(get_db)):
    blog_object = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_object:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"No Blog Available with id {id}")
    if blog.title:
        blog_object.title = blog.title
    if blog.body:
        blog_object.body = blog.body
    
    db.commit()
    db.refresh(blog_object)
    return blog_object
















# @app.get("/blog")
# def get_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}")
# def get_blog(id:int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     return blog

# @app.delete("/blog/{id}")
# def delete_blog(id:int, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return {"message": "Blog deleted successfully"}

# @app.put("/blog/{id}")
# def update_blog(id:int, blog: Blog, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).update({"title": blog.title, "body": blog.body})
#     db.commit()
#     return {"message": "Blog updated successfully"}