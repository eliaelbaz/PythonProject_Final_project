from pydantic import BaseModel

class UserSignup(BaseModel):
    username: str
    password: str

class UserDelete(BaseModel):
    username: str
    password: str

class AddTokensRequest(BaseModel):
    username: str
    credit_card: str
    amount: int