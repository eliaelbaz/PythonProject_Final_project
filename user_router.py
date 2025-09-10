from fastapi import APIRouter, HTTPException
from user_model import UserSignup, UserDelete, AddTokensRequest
import user_service

router = APIRouter()

user_service.create_users_table()

@router.post("/signup")
def signup(data: UserSignup):
    if user_service.signup_user(data.username, data.password):
        return {"message": "User created"}
    raise HTTPException(status_code=400, detail="Username already exists")

@router.delete("/remove_user")
def delete_user(data: UserDelete):
    if user_service.delete_user(data.username, data.password):
        return {"message": "User deleted"}
    raise HTTPException(status_code=404, detail="User not found")

@router.get("/tokens/{username}")
def get_tokens(username: str):
    tokens = user_service.get_tokens(username)
    if tokens is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"tokens": tokens}

@router.post("/add_tokens")
def add_tokens(data: AddTokensRequest):
    if user_service.add_tokens(data.username, data.amount):
        return {"message": f"Added {data.amount} tokens to {data.username}"}
    raise HTTPException(status_code=404, detail="User not found")