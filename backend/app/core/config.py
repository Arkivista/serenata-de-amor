"""Configuração mínima e auditável do backend.

Este módulo evita segredos no código. Valores sensíveis devem vir de variáveis
de ambiente ou de arquivos `.env` não versionados.
"""

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    """Configurações do backend do MVP de LEDs."""

    app_name: str = "Sistema de Apoio à Análise de LEDs"
    app_version: str = "0.1.0"
    environment: str = "development"
    database_url: str = "postgresql+psycopg://led:led@led-db:5432/led"
    storage_path: str = "/data/uploads"
    max_upload_size_mb: int = 50
    ai_enabled: bool = False


def get_settings() -> Settings:
    """Carrega configurações por variáveis de ambiente.

    Mantém IA desligada por padrão para cumprir o princípio arquitetural do MVP.
    """

    return Settings(
        environment=os.getenv("LED_ENVIRONMENT", Settings.environment),
        database_url=os.getenv("LED_DATABASE_URL", Settings.database_url),
        storage_path=os.getenv("LED_STORAGE_PATH", Settings.storage_path),
        max_upload_size_mb=int(os.getenv("LED_MAX_UPLOAD_SIZE_MB", Settings.max_upload_size_mb)),
        ai_enabled=os.getenv("LED_AI_ENABLED", "false").lower() == "true",
    )
