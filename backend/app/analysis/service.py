"""Serviço de análise estruturada em lote para o protótipo funcional."""

from collections import Counter

from app.analysis.models import LineAnalysisResult, StructuredAnalysisRequest, StructuredAnalysisResult
from app.rules.engine import evaluate_led_line


def evaluate_structured_analysis(request: StructuredAnalysisRequest) -> StructuredAnalysisResult:
    """Executa regras para várias linhas de LED já estruturadas.

    Esta etapa permite validar o fluxo de comparação antes de integrar extração
    de PDF, revisão humana, banco de dados e interface completa.
    """

    line_results = [
        LineAnalysisResult(
            line_id=line.line_id,
            codigo=line.codigo,
            results=evaluate_led_line(line, request.approved_items),
        )
        for line in request.led_lines
    ]
    counter: Counter[str] = Counter()
    for line_result in line_results:
        for rule_result in line_result.results:
            counter[rule_result.status] += 1
    return StructuredAnalysisResult(
        analysis_id=request.analysis_id,
        line_results=line_results,
        summary=dict(sorted(counter.items())),
    )
