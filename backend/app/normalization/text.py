"""Normalização textual controlada para comparação determinística."""

from dataclasses import dataclass
import re
import unicodedata

NORMALIZER_VERSION = "0.1.0"


@dataclass(frozen=True)
class NormalizedValue:
    """Valor original, valor normalizado e regra aplicada."""

    original: str | None
    normalized: str
    rule: str
    version: str = NORMALIZER_VERSION


def normalize_whitespace(value: str | None) -> NormalizedValue:
    """Remove espaços duplicados sem alterar o sentido do texto."""

    original = value
    normalized = re.sub(r"\s+", " ", value or "").strip()
    return NormalizedValue(original=original, normalized=normalized, rule="normalize_whitespace")


def normalize_for_comparison(value: str | None) -> NormalizedValue:
    """Normaliza texto para comparação: espaços, caixa e acentos.

    O valor original deve sempre ser preservado fora desta função.
    """

    compact = normalize_whitespace(value).normalized.casefold()
    without_accents = "".join(
        char for char in unicodedata.normalize("NFD", compact) if unicodedata.category(char) != "Mn"
    )
    return NormalizedValue(
        original=value,
        normalized=without_accents,
        rule="normalize_whitespace_casefold_remove_accents",
    )
