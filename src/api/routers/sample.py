import logging

from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter(tags=["Sample"])


class HelloWorld(BaseModel):
    message: str


@router.get("/hello-world", response_model=HelloWorld)
async def hello_world():
    # ログを出力する
    # print("Hello world")
    logging.info("Hello world")
    return HelloWorld(message="Hello world2")


class Result(BaseModel):
    result: str


@router.get("/free-word-search", response_model=Result)
async def free_word_search(word: str = "sample"):
    # # example.comにアクセスして、wordを検索する
    # ret = requests.get(f"https://example.com/search?q={word}")
    # # logを出力する
    # logger.info(f"word: {word}, status_code: {ret.status_code}")
    return Result(result=f"Hello {word}")
