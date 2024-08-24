# Importing the necessary libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Defining the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Creating an engine for the database
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creating a session local, which will be used to create a session for the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creating a base class because we will be creating models
Base = declarative_base()