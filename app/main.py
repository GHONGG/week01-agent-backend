import logging
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from app.core.config import settings
from app.core.logging import logger, setup_logging
from app.routers import chat, health

setup_logging(level=logging.DEBUG if settings.debug else logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """服务启动和关闭时各执行一次"""
    logger.info("服务启动: %s (debug=%s)", settings.app_name, settings.debug)
    yield
    logger.info("服务关闭")


app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    lifespan=lifespan,
)
app.include_router(health.router)
app.include_router(chat.router)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
    )
