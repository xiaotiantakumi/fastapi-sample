from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()


class HelloWorld(BaseModel):
    message: str


@app.get("/hello-world", response_model=HelloWorld)
async def hello_world():
    return HelloWorld(message="Hello world5")