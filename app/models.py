from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str

class PostCreate(BaseModel):
    user_id:str
    content:str

class FollowRequest(BaseModel):
    user_id:str
    target_id:str

class LikeRequest(BaseModel):
    user_id:str
    post_id:str

