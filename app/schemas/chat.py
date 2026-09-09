from pydantic import BaseModel, Field


class HealthResponse(BaseModel):
    """健康检查的响应结构"""

    status: str = "ok"
    app_name: str
    debug: bool


class ChatRequest(BaseModel):
    """聊天请求：校验用户输入"""

    message: str = Field(..., min_length=1, max_length=2000)
    session_id: str = Field(default="default", min_length=1, max_length=64)


class ChatResponse(BaseModel):
    """聊天响应"""

    reply: str
    length: int
    session_id: str
    request_id: str


class HistoryItem(BaseModel):
    role: str
    content: str


class HistoryResponse(BaseModel):
    session_id: str
    limit: int
    total: int
    items: list[HistoryItem]
