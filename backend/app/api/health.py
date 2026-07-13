"""Endpoint de saúde para validar que o backend iniciou."""

from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["saúde"])


@router.get("/health", summary="Verificar saúde da API")
def health_check() -> dict[str, str | bool]:
    """Retorna estado básico da API sem expor informações sensíveis."""

    settings = get_settings()
    return {
        "status": "ok",
        "service": settings.app_name,
        "version": settings.app_version,
        "ai_enabled": settings.ai_enabled,
    }
