from fastapi import APIRouter
from app.db import get_session
from app.models import FollowRequest

router = APIRouter(prefix="/social", tags=["Social"])

@router.post("/follow")
def follow_user(data:FollowRequest):
    with get_session() as session:
        query ="""
        MATCH (u:User {id: $user_id})
        MATCH (t:User {id: $target_id})
        MERGE (u)-[:FOLLOWS]->(t)
        """
        session.run(
            query,
            user_id=data.user_id,
            target_id=data.target_id
        )


@router.get("/feed{user_id}")
def get_feed(user_id:str):
    with get_session() as session:
        query ="""
        MATCH (u:User {id: $user_id})-[:FOLLOWS]->(f:User)
        MATCH (f)-[:CREATED]->(p:Post)
        RETURNN p ORDER BY p.id DESC
        """

        result = session.run(query, user_id=user_id)
        return [record["p"] for record in result]