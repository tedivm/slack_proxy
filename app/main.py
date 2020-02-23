import logging
import os
from typing import Dict, Any
import aiohttp
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import Response

assert 'SLACK_WEBHOOK' in os.environ

logger = logging.getLogger("api")
logger.setLevel(logging.DEBUG)

app = FastAPI()


@app.post('/')
async def webhook(body: Dict[str, Any]):
    logger.debug(body)
    async with aiohttp.ClientSession() as session:
        async with session.post(os.environ['SLACK_WEBHOOK'], json=body) as resp:
            status = resp.status
            content = await resp.text()
    return Response(status_code=status, content=content)
