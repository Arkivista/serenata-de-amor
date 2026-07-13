"""Execução determinística das primeiras regras do MVP."""

from collections.abc import Iterable

from app.normalization.code import normalize_code
from app.normalization.text import normalize_for_comparison
from app.rules.models import LedLine, RuleResult, TemporalidadeItem

RULE_VERSION = "0.1.0"


COMMENT_BY_RULE = {
    "LED-COD-001": "Rever o código de classificação informado, pois ele não foi localizado na tabela de temporalidade selecionada.",
    "LED-DES-001": "Adequar o descritor ao código de classificação correspondente.",
    "LED-TEMP-001": "Corrigir o prazo de guarda na fase corrente, conforme estabelecido na tabela de temporalidade.",
    "LED-TEMP-003": "Corrigir o prazo de guarda na fase intermediária, conforme estabelecido na tabela de temporalidade.",
    "LED-DEST-001": "Corrigir a destinação final, observando a previsão estabelecida na tabela de temporalidade aplicável.",
    "LED-OBS-001": "Esclarecer o atendimento à condição especial prevista na tabela de temporalidade.",
}


def _missing(value: str | None) -> bool:
    return value is None or value.strip() == ""


def _compare_text(led_value: str | None, expected_value: str | None) -> tuple[str, str]:
    led_normalized = normalize_for_comparison(led_value).normalized
    expected_normalized = normalize_for_comparison(expected_value).normalized
    if _missing(led_value):
        return "INFORMAÇÃO AUSENTE", led_normalized
    if led_normalized == expected_normalized:
        return "CONFORME", led_normalized
    return "DIVERGENTE", led_normalized


def _result(
    *,
    rule_id: str,
    field: str,
    status: str,
    led_value_original: str | None,
    led_value_normalized: str,
    expected_value: str | None,
    requires_human_validation: bool = False,
) -> RuleResult:
    return RuleResult(
        rule_id=rule_id,
        rule_version=RULE_VERSION,
        field=field,
        status=status,
        led_value_original=led_value_original,
        led_value_normalized=led_value_normalized,
        expected_value=expected_value,
        message=COMMENT_BY_RULE[rule_id],
        requires_human_validation=requires_human_validation,
    )


def find_temporalidade_item(
    led_code: str | None,
    approved_items: Iterable[TemporalidadeItem],
) -> TemporalidadeItem | None:
    """Localiza item aprovado por código normalizado sem remover pontuação."""

    normalized_led_code = normalize_code(led_code).normalized
    for item in approved_items:
        if item.status_validacao != "aprovado":
            continue
        if normalize_code(item.codigo).normalized == normalized_led_code:
            return item
    return None


def evaluate_led_line(
    led_line: LedLine,
    approved_items: Iterable[TemporalidadeItem],
) -> list[RuleResult]:
    """Compara uma linha estruturada de LED com itens aprovados da tabela."""

    item = find_temporalidade_item(led_line.codigo, approved_items)
    normalized_code = normalize_code(led_line.codigo).normalized
    if item is None:
        return [
            _result(
                rule_id="LED-COD-001",
                field="codigo",
                status="CÓDIGO NÃO LOCALIZADO",
                led_value_original=led_line.codigo,
                led_value_normalized=normalized_code,
                expected_value=None,
                requires_human_validation=True,
            )
        ]

    results = [
        _result(
            rule_id="LED-COD-001",
            field="codigo",
            status="CONFORME",
            led_value_original=led_line.codigo,
            led_value_normalized=normalized_code,
            expected_value=item.codigo,
        )
    ]

    status, normalized = _compare_text(led_line.descritor, item.descritor)
    results.append(
        _result(
            rule_id="LED-DES-001",
            field="descritor",
            status=status,
            led_value_original=led_line.descritor,
            led_value_normalized=normalized,
            expected_value=item.descritor,
            requires_human_validation=status != "CONFORME",
        )
    )

    status, normalized = _compare_text(led_line.prazo_corrente, item.prazo_corrente)
    results.append(
        _result(
            rule_id="LED-TEMP-001",
            field="prazo_corrente",
            status=status,
            led_value_original=led_line.prazo_corrente,
            led_value_normalized=normalized,
            expected_value=item.prazo_corrente,
            requires_human_validation=status != "CONFORME",
        )
    )

    status, normalized = _compare_text(led_line.prazo_intermediario, item.prazo_intermediario)
    results.append(
        _result(
            rule_id="LED-TEMP-003",
            field="prazo_intermediario",
            status=status,
            led_value_original=led_line.prazo_intermediario,
            led_value_normalized=normalized,
            expected_value=item.prazo_intermediario,
            requires_human_validation=status != "CONFORME",
        )
    )

    status, normalized = _compare_text(led_line.destinacao_final, item.destinacao_final)
    results.append(
        _result(
            rule_id="LED-DEST-001",
            field="destinacao_final",
            status=status,
            led_value_original=led_line.destinacao_final,
            led_value_normalized=normalized,
            expected_value=item.destinacao_final,
            requires_human_validation=status != "CONFORME",
        )
    )

    if item.observacao:
        results.append(
            _result(
                rule_id="LED-OBS-001",
                field="observacao",
                status="NECESSITA ANÁLISE HUMANA",
                led_value_original=None,
                led_value_normalized="",
                expected_value=item.observacao,
                requires_human_validation=True,
            )
        )

    return results
