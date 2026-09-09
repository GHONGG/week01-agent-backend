from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query, status

from app.core.deps import get_request_id, verify_api_key
from app.schemas.chat import (
    ChatRequest,
    ChatResponse,
    HistoryResponse,
)
from app.services import agent

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("", response_model=ChatResponse)
def chat(
    payload: ChatRequest,
    request_id: Annotated[str, Depends(get_request_id)],
) -> ChatResponse:
    """聊天接口：接收消息并返回处理结果"""
    reply, length = agent.echo_message(payload.message)
    return ChatResponse(
        reply=reply,
        length=length,
        session_id=payload.session_id,
        request_id=request_id,
    )


@router.get("/history/{session_id}", response_model=HistoryResponse)
def history(
    session_id: Annotated[
        str, Path(min_length=1, max_length=64, description="会话 ID")
    ],
    limit: Annotated[int, Query(ge=1, le=100, description="返回条数")] = 10,
) -> HistoryResponse:
    """演示路径参数 + 查询参数。

    session_id 来自 URL 路径，limit 来自 ?limit=20 这样的查询串。
    传入 session_id=unknown 会触发 404。
    """
    items = agent.fake_history(session_id, limit)
    if not items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"会话 {session_id} 不存在",
        )
    return HistoryResponse(
        session_id=session_id,
        limit=limit,
        total=len(items),
        items=items,
    )


@router.post("/secure", response_model=ChatResponse)
def secure_chat(
    payload: ChatRequest,
    request_id: Annotated[str, Depends(get_request_id)],
    _verified: Annotated[None, Depends(verify_api_key)],
) -> ChatResponse:
    """需要 API Key 的接口：演示依赖注入做鉴权。

    请求头里带 X-API-Key，值要等于 .env 里的 API_KEY。
    """
    reply, length = agent.echo_message(payload.message)
    return ChatResponse(
        reply=reply,
        length=length,
        session_id=payload.session_id,
        request_id=request_id,
    )
