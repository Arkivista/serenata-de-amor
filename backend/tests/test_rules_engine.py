from app.rules.engine import evaluate_led_line
from app.rules.models import LedLine, TemporalidadeItem


def test_demo_line_matches_expected_mvp_results():
    table_items = [
        TemporalidadeItem(
            codigo="023.15",
            descritor="Controle de frequência",
            prazo_corrente="5 anos",
            prazo_intermediario="não se aplica",
            destinacao_final="eliminação",
        )
    ]
    led_line = LedLine(
        line_id="linha-1",
        codigo="023.15",
        descritor="Folhas de frequência",
        prazo_corrente="5 anos",
        prazo_intermediario="não se aplica",
        destinacao_final="guarda permanente",
    )

    results = {result.rule_id: result for result in evaluate_led_line(led_line, table_items)}

    assert results["LED-COD-001"].status == "CONFORME"
    assert results["LED-DES-001"].status == "DIVERGENTE"
    assert results["LED-TEMP-001"].status == "CONFORME"
    assert results["LED-TEMP-003"].status == "CONFORME"
    assert results["LED-DEST-001"].status == "DIVERGENTE"


def test_unknown_code_requires_human_validation():
    results = evaluate_led_line(
        LedLine(line_id="linha-2", codigo="999.99"),
        [TemporalidadeItem(codigo="023.15", descritor="Controle de frequência")],
    )

    assert len(results) == 1
    assert results[0].rule_id == "LED-COD-001"
    assert results[0].status == "CÓDIGO NÃO LOCALIZADO"
    assert results[0].requires_human_validation is True


def test_item_with_observation_generates_human_analysis_result():
    results = evaluate_led_line(
        LedLine(
            line_id="linha-3",
            codigo="023.15",
            descritor="Controle de frequência",
            prazo_corrente="5 anos",
            prazo_intermediario="não se aplica",
            destinacao_final="eliminação",
        ),
        [
            TemporalidadeItem(
                codigo="023.15",
                descritor="Controle de frequência",
                prazo_corrente="5 anos",
                prazo_intermediario="não se aplica",
                destinacao_final="eliminação",
                observacao="Verificar condição especial fictícia.",
            )
        ],
    )

    assert results[-1].rule_id == "LED-OBS-001"
    assert results[-1].status == "NECESSITA ANÁLISE HUMANA"
    assert results[-1].requires_human_validation is True
