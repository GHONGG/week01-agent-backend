import logging

from app.schemas.chat import HistoryItem

logger = logging.getLogger("app")


def build_health(app_name: str, debug: bool) -> dict[str, object]:
    """构造健康检查数据"""
    logger.info("健康检查被调用: app=%s debug=%s", app_name, debug)
    return {"status": "ok", "app_name": app_name, "debug": debug}


def echo_message(message: str) -> tuple[str, int]:
    """示例业务逻辑：原样返回输入，并统计长度"""
    logger.info("收到消息，长度 %d", len(message))
    return f"收到：{message}", len(message)


def fake_history(session_id: str, limit: int) -> list[HistoryItem]:
    """假的会话历史，用来演示路径参数 + 查询参数"""
    if session_id == "unknown":
        return []

    pool = [
        HistoryItem(role="user", content="你好"),
        HistoryItem(role="assistant", content="你好，有什么可以帮你？"),
        HistoryItem(role="user", content="讲讲 FastAPI"),
        HistoryItem(role="assistant", content="FastAPI 是一个现代 Python Web 框架"),
    ]
    logger.info("查询历史: session=%s limit=%d", session_id, limit)
    return pool[:limit]
