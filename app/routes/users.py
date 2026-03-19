from fastapi import APIRouter
from app.db import get_session
from app.models import UserCreate

router=APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def create_user(user: UserCreate):
    with get_session() as session:
        query = """
        CREATE (u:User {id: randomUUID(), name: $name})
        RETURN u                
        """
        result = session.run(query, name=user.name)
        record=result.single()
        return record["u"]

@router.get("/")
def get_user():
    with get_session() as session:
        query = "MATCH (u:User) RETURN u"
        result = session.run(query)
        return [record["u"] for record in result]

'''
I want to create a simple neo4j based social-netowk application
Tech stack: Python, Fastapi, neo4j
so please help me
'''