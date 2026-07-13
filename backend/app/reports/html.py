"""Relatório HTML simples para resultados estruturados do protótipo."""

from html import escape

from app.analysis.models import StructuredAnalysisResult


def generate_structured_analysis_html(result: StructuredAnalysisResult) -> str:
    """Gera HTML auditável e estático com síntese e resultados detalhados."""

    summary_rows = "".join(
        f"<tr><td>{escape(status)}</td><td>{count}</td></tr>" for status, count in result.summary.items()
    )
    detail_rows = []
    for line_result in result.line_results:
        for rule_result in line_result.results:
            detail_rows.append(
                "<tr>"
                f"<td>{escape(line_result.line_id)}</td>"
                f"<td>{escape(line_result.codigo or '')}</td>"
                f"<td>{escape(rule_result.rule_id)}</td>"
                f"<td>{escape(rule_result.field)}</td>"
                f"<td>{escape(rule_result.status)}</td>"
                f"<td>{escape(rule_result.led_value_original or '')}</td>"
                f"<td>{escape(rule_result.expected_value or '')}</td>"
                f"<td>{escape(rule_result.message)}</td>"
                f"<td>{'sim' if rule_result.requires_human_validation else 'não'}</td>"
                "</tr>"
            )
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <title>Relatório preliminar da análise {escape(result.analysis_id)}</title>
</head>
<body>
  <h1>Relatório preliminar da análise {escape(result.analysis_id)}</h1>
  <p>Este relatório é gerado a partir de dados estruturados de teste ou revisados manualmente. Ele não substitui a decisão do arquivista.</p>
  <h2>Síntese</h2>
  <table>
    <thead><tr><th>Resultado</th><th>Total</th></tr></thead>
    <tbody>{summary_rows}</tbody>
  </table>
  <h2>Resultados detalhados</h2>
  <table>
    <thead><tr><th>Linha</th><th>Código</th><th>Regra</th><th>Campo</th><th>Resultado</th><th>Valor na LED</th><th>Valor esperado</th><th>Comentário sugerido</th><th>Validação humana</th></tr></thead>
    <tbody>{''.join(detail_rows)}</tbody>
  </table>
</body>
</html>"""
