from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from typing import List
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

app = FastAPI()

users = []


class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/")
async def get_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get("/user/{user_id}")
async def get_user(request: Request, user_id: int) -> HTMLResponse:
    for u in users:
        if u.id == user_id:
            return templates.TemplateResponse("users.html", {"request": request, "user": u})
    raise HTTPException(status_code=404, detail="User was not found")
    # return templates.TemplateResponse("users.html", {"request": request,
    #                                                  "user": User(id=user_id, username="Error User not found", age=0)})


@app.post("/user/{username}/{age}")
async def post_add_user(usr: User) -> str:
    usr_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=usr_id, username=usr.username, age=usr.age)
    users.append(new_user)
    return f"User {new_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_update_user(user_id: int, usr: User) -> str:
    for u in users:
        if u.id == user_id:
            u.username = usr.username
            u.age = usr.age
            return f"The user {u} is updated"
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    for i, u in enumerate(users):
        if u.id == user_id:
            usr_del = users.pop(i)
            return f"User {usr_del} has been deleted"
    raise HTTPException(status_code=404, detail="User was not found")
