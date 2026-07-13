from app.core.config import get_settings


def test_ai_is_disabled_by_default(monkeypatch):
    monkeypatch.delenv("LED_AI_ENABLED", raising=False)

    settings = get_settings()

    assert settings.ai_enabled is False


def test_environment_can_be_configured(monkeypatch):
    monkeypatch.setenv("LED_ENVIRONMENT", "test")

    settings = get_settings()

    assert settings.environment == "test"
