from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
        title="Fast API LMS",
        description="LMS for managing students and courses.",
        version="0.0.1"
    )

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str] = None


@app.get("/", response_model=List[User])
async def get_users():
    return users


@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return {"User": "Created"}


@app.get("/{id}")
async def get_user(id: int = Path(..., description="Id of User")):
    return users[id]
