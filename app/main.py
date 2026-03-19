from fastapi import FastAPI
from app.routes import users, posts, social
from app.db import test_connection

app = FastAPI(title="Neo4j Social Network")

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(social.router)

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/test-db")
def test_db():
    return {"status": test_connection()}