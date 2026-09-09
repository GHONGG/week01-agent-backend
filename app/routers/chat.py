from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services import agent

router = APIRouter(tags=["chat"])


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    """聊天接口：接收消息并返回处理结果"""
    reply, length = agent.echo_message(payload.message)
    return ChatResponse(reply=reply, length=length)
