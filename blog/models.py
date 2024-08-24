from .database import Base
from sqlalchemy import Column, Integer, String, Boolean

# Creating a model for the blog
class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String, nullable=True)
    published = Column(Boolean, default=True)
