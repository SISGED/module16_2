from fastapi import FastAPI, Path
from typing import Annotated

app=FastAPI()

@app.get("/")
async def main_page():
    return "Главная страница"

@app.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(ge=5, le=20,
                                             description="Enter username",
                                             examples="UrbanUser")],
               age: Annotated[int, Path(ge=18, le=120,
                                       description="Enter age",
                                       examples="24")]) -> dict:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/{user_id}")
async def id(user_id: Annotated[int, Path (ge=1, le=100,
                                           description='Enter User ID',
                                           examples="1")]):
    return f"Вы вошли как пользователь №{user_id}!"

@app.get("/user/admin")
async def admin():
    return"Вы вошли как администратор!"
