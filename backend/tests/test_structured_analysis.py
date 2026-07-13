from app.analysis.models import StructuredAnalysisRequest
from app.analysis.service import evaluate_structured_analysis
from app.reports.html import generate_structured_analysis_html
from app.rules.models import LedLine, TemporalidadeItem


def _request() -> StructuredAnalysisRequest:
    return StructuredAnalysisRequest(
        analysis_id="analise-ficticia-1",
        approved_items=[
            TemporalidadeItem(
                codigo="023.15",
                descritor="Controle de frequência",
                prazo_corrente="5 anos",
                prazo_intermediario="não se aplica",
                destinacao_final="eliminação",
            )
        ],
        led_lines=[
            LedLine(
                line_id="linha-1",
                codigo="023.15",
                descritor="Controle de frequência",
                prazo_corrente="5 anos",
                prazo_intermediario="não se aplica",
                destinacao_final="eliminação",
            ),
            LedLine(
                line_id="linha-2",
                codigo="023.15",
                descritor="Folhas de frequência",
                prazo_corrente="5 anos",
                prazo_intermediario="não se aplica",
                destinacao_final="guarda permanente",
            ),
        ],
    )


def test_evaluate_structured_analysis_summarizes_multiple_lines():
    result = evaluate_structured_analysis(_request())

    assert result.analysis_id == "analise-ficticia-1"
    assert len(result.line_results) == 2
    assert result.summary["CONFORME"] == 8
    assert result.summary["DIVERGENTE"] == 2


def test_generate_structured_analysis_html_contains_summary_and_details():
    result = evaluate_structured_analysis(_request())
    html = generate_structured_analysis_html(result)

    assert "Relatório preliminar da análise analise-ficticia-1" in html
    assert "DIVERGENTE" in html
    assert "Corrigir a destinação final" in html
