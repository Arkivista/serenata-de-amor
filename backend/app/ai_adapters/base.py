"""Contrato para integrações futuras de IA.

A interface existe para manter qualquer IA fora do motor determinístico de regras.
Implementações futuras deverão registrar fornecedor, modelo, dados usados,
confiança, finalidade e validação humana.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class AISuggestion:
    """Sugestão auxiliar produzida por IA, nunca decisão definitiva."""

    suggestion: str
    confidence: float
    model: str
    provider: str
    requires_human_validation: bool = True


class AIAdapter(Protocol):
    """Interface para serviços opcionais de IA."""

    def suggest(self, *, purpose: str, input_summary: str) -> AISuggestion:
        """Retorna sugestão auxiliar para validação humana."""
