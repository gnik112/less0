from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/")
async def get_root() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_add_user(
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def put_update_user(
        user_id: Annotated[int, Path(ge=1, description='User ID', example='2')],
        username: Annotated[str, Path(min_length=3, max_length=20, description='Enter username', example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='28')]) -> str:
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(
        user_id: Annotated[int, Path(ge=1, description='User ID', example='2')]) -> str:
    try:
        del users[str(user_id)]
    except KeyError:
        return f"No such key: {user_id}"
    return f"User {user_id} has been deleted"
