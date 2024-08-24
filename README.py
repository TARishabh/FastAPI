"""
WHY FASTAPI?

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.

ASYNC PROGRAMMING
TYPE HINTS (PYDANTIC)
DEFAULT SWAGGER DOCS, REDOC
OPENAPI and JSON SCHEMA
SECURITY AND AUTHENTICATION
DEPENDENCY INJECTION


STARLETTE FEATURES
WEB SOCKETS SUPPORT
GRAPHQL SUPPORT
INPROCESS BACKGROUND TASKS
STARTUPS AND SHUTDOWN EVENTS


SQL DATA
NO SQL DATABASE
GRAPH DATABASE


To start a new project with FastAPI, you can use the following command:

Create a virtual environment
$ python3 -m venv myenv
$ source myenv/bin/activate

Install FastAPI
$ pip install fastapi

Install Uvicorn
$ pip install uvicorn

Create a new file main.py and after that, you can run the server with the following command:
$ uvicorn main:app --reload

PS:- main is the name of the file and app is the name of the FastAPI instance.

Terminology:
('/'): Path or Endpoint 
.get(): Operation or  HTTP Method 
@app: path operation decorator
def home(): path operation function
{"message": "Hello World"}: Response Model

to change port number for debugging:
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

Now we have to connect to database, we can use SQLAlchemy for this purpose.

$ pip install sqlalchemy

The difference between schema and model is that schema is used for validation and model is used for database operations.

That means the schema is a pydantic model and the model is a SQLAlchemy model.

To create a database connection, we can use the following command:

create a new file database.py:

now after writing the code in database.py, we can import the engine and SessionLocal in main.py and create a new database session in the path operation function.

then we can create a new file models.py and create a Pydantic model for the blog.

now, in main.py, use:
models.Base.metadata.create_all(bind=engine)


"""
