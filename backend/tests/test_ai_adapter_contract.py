from app.ai_adapters.base import AISuggestion


def test_ai_suggestion_requires_human_validation_by_default():
    suggestion = AISuggestion(
        suggestion="Sugerir possível correspondência de descritor.",
        confidence=0.42,
        model="modelo-ficticio",
        provider="provedor-ficticio",
    )

    assert suggestion.requires_human_validation is True
