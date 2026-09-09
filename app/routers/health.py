from fastapi import APIRouter

from app.core.config import settings
from app.schemas.chat import HealthResponse
from app.services import agent

router = APIRouter(tags=["health"])


@router.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """健康检查接口"""
    data = agent.build_health(settings.app_name, settings.debug)
    return HealthResponse(**data)
