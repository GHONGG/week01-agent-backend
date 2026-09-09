"""依赖注入示例：把"每次请求都要做的事"抽出来复用"""

import uuid

from fastapi import Header, HTTPException, status

from app.core.config import settings
from app.core.logging import logger


def get_request_id(x_request_id: str | None = Header(default=None)) -> str:
    """读取客户端传来的请求 ID，没传就生成一个。

    用法：在路由函数参数里写 Depends(get_request_id)，
    FastAPI 会自动调用它并把返回值注入进来。
    """
    request_id = x_request_id or uuid.uuid4().hex[:8]
    logger.info("请求进入, request_id=%s", request_id)
    return request_id


def verify_api_key(x_api_key: str | None = Header(default=None)) -> None:
    """校验 API Key。

    settings.api_key 为空表示"不启用校验"（方便本地开发）。
    """
    if not settings.api_key:
        return
    if x_api_key != settings.api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key 无效",
        )
