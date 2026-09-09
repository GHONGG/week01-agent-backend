"""SSE 流式输出：async 的实战场景"""

import asyncio
from collections.abc import AsyncIterator
from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse

from app.core.logging import logger

router = APIRouter(prefix="/stream", tags=["stream"])


async def token_generator(message: str) -> AsyncIterator[str]:
    """把一句话一个字一个字吐出来，模拟大模型流式返回。

    async + yield = 异步生成器。每次 yield 之后控制权交回事件循环，
    服务器可以去处理别的请求，不会卡住。
    """
    logger.info("开始流式输出: %s", message)
    for char in message:
        yield f"data: {char}\n\n"
        await asyncio.sleep(0.15)
    yield "data: [DONE]\n\n"


@router.get("")
async def stream(
    message: Annotated[str, Query(min_length=1, max_length=100)] = "你好，我是流式输出",
) -> StreamingResponse:
    """SSE 接口。浏览器用 EventSource 或 fetch 逐段读取。"""
    return StreamingResponse(
        token_generator(message),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
        },
    )
