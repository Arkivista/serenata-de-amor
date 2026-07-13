"""Normalização controlada de códigos de classificação."""

from app.normalization.text import NormalizedValue, normalize_whitespace

CODE_NORMALIZER_VERSION = "0.1.0"


def normalize_code(value: str | None) -> NormalizedValue:
    """Normaliza código sem remover zeros, pontos ou hífens.

    A primeira versão remove apenas espaços duplicados e espaços externos para
    evitar uma normalização arquivisticamente agressiva.
    """

    normalized = normalize_whitespace(value).normalized
    return NormalizedValue(
        original=value,
        normalized=normalized,
        rule="normalize_code_trim_spaces_preserve_punctuation",
        version=CODE_NORMALIZER_VERSION,
    )
