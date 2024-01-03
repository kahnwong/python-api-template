from datetime import datetime

from fastapi import FastAPI

from python_api_template.model.request import RequestItem
from python_api_template.model.response import ResponseItem
from python_api_template.utils.log import logger

app = FastAPI(title="python_api_template")


#######################
# routes
#######################
@app.get("/version")
async def root():
    return {"version": "0.1.0"}


@app.post("/", response_model=ResponseItem)
async def main(request: RequestItem) -> ResponseItem:
    logger.info(f"Input: {request}")

    return ResponseItem(time=datetime.now(), message=request.message)
