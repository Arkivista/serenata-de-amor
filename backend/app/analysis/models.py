"""Modelos da análise estruturada sem dependência inicial de banco de dados."""

from dataclasses import dataclass, field

from app.rules.models import LedLine, RuleResult, TemporalidadeItem


@dataclass(frozen=True)
class StructuredAnalysisRequest:
    """Entrada do protótipo plenamente testável sem extração de PDF."""

    analysis_id: str
    led_lines: list[LedLine]
    approved_items: list[TemporalidadeItem]


@dataclass(frozen=True)
class LineAnalysisResult:
    """Resultados de regras para uma linha de LED."""

    line_id: str
    codigo: str | None
    results: list[RuleResult]


@dataclass(frozen=True)
class StructuredAnalysisResult:
    """Resultado consolidado de uma análise estruturada."""

    analysis_id: str
    line_results: list[LineAnalysisResult]
    summary: dict[str, int] = field(default_factory=dict)
