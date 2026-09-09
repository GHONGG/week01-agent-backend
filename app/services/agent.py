import logging

logger = logging.getLogger("app")


def build_health(app_name: str, debug: bool) -> dict[str, object]:
    """构造健康检查数据"""
    logger.info("健康检查被调用: app=%s debug=%s", app_name, debug)
    return {"status": "ok", "app_name": app_name, "debug": debug}


def echo_message(message: str) -> tuple[str, int]:
    """示例业务逻辑：原样返回输入，并统计长度"""
    logger.info("收到消息，长度 %d", len(message))
    return f"收到：{message}", len(message)
