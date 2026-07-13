"""Rotas de protótipo para análise estruturada em lote."""

from fastapi import APIRouter

from app.analysis.models import StructuredAnalysisRequest, StructuredAnalysisResult
from app.analysis.service import evaluate_structured_analysis
from app.reports.html import generate_structured_analysis_html

router = APIRouter(prefix="/analyses", tags=["análises"])


@router.post("/evaluate-structured", response_model=StructuredAnalysisResult)
def evaluate_structured(request: StructuredAnalysisRequest) -> StructuredAnalysisResult:
    """Executa análise em lote com dados estruturados, sem depender de PDF."""

    return evaluate_structured_analysis(request)


@router.post("/evaluate-structured/report-html", response_model=str)
def evaluate_structured_report_html(request: StructuredAnalysisRequest) -> str:
    """Executa análise estruturada e retorna relatório HTML preliminar."""

    return generate_structured_analysis_html(evaluate_structured_analysis(request))
