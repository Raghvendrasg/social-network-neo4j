from fastapi import APIRouter
from app.db import get_session
from app.models import PostCreate, LikeRequest

router= APIRouter(prefix="/posts", tags=["Posts"])

@router.post("/")
def create_post(post:PostCreate):
    with get_session() as session:
        query="""
        MATCH (u:User {id: $user_id})
        CREATE (p:Post {id: randomUUID(), content: $content})
        CREATE (u)-[:CREATED]->(p)
        RETURN p
        """

        result=session.run(
            query,
            user_id=post.user_id,
            content=post.content
        )

        return result.single()["p"]
    

@router.post("/like")
def like_post(data: LikeRequest):
    with get_session() as session:
        query = """
        MATCH (u:User {id: $user_id})
        MATCH (p:Post {id: $post_id})
        MERGE (u)-[:LIKED]->(p)
        """
        session.run(query,user_id=data.user_id, post_id=data.post_id)

        return {"message": "Post Liked"}