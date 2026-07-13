"""Rotas de protótipo para testar o motor determinístico de regras."""

from dataclasses import dataclass

from fastapi import APIRouter

from app.rules.engine import evaluate_led_line
from app.rules.models import LedLine, RuleResult, TemporalidadeItem

router = APIRouter(prefix="/rules", tags=["regras"])


@dataclass(frozen=True)
class EvaluateLineRequest:
    """Entrada estruturada para comparar uma linha de LED com a tabela aprovada."""

    led_line: LedLine
    approved_items: list[TemporalidadeItem]


@router.post("/evaluate-line", response_model=list[RuleResult])
def evaluate_line(request: EvaluateLineRequest) -> list[RuleResult]:
    """Executa regras determinísticas sem depender de extração de PDF."""

    return evaluate_led_line(request.led_line, request.approved_items)
