# from sqlmodel import Field, Session, SQLModel, create_engine, select, Sequence
from fastapi import FastAPI, Depends

my_service = FastAPI(title="My Service API", 
    version="0.0.1",
    servers=[
        {
            "url": "http://localhost:8000", # ADD NGROK URL Here Before Creating GPT Action
            "description": "Development Server"
        }
        ])

@my_service.get("/")
def read_root():
    return {"Welcome": "My First User Service of Online Mart"}
