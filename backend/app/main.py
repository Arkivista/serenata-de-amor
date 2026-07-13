"""Aplicação FastAPI mínima para o MVP de análise de LEDs."""

from fastapi import FastAPI

from app.api.analyses import router as analyses_router
from app.api.documents import router as documents_router
from app.api.health import router as health_router
from app.api.rules import router as rules_router
from app.core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description=(
        "API inicial do sistema de apoio à análise de Listagens de "
        "Eliminação de Documentos. O MVP não utiliza IA no núcleo decisório."
    ),
)

app.include_router(health_router)
app.include_router(analyses_router)
app.include_router(rules_router)
app.include_router(documents_router)
