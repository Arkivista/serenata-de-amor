"""Modelos simples para linhas estruturadas e resultados de regras."""

from dataclasses import dataclass

RULE_ENGINE_VERSION = "0.1.0"


@dataclass(frozen=True)
class LedLine:
    """Linha de LED já extraída ou digitada em estrutura mínima."""

    line_id: str
    codigo: str | None = None
    descritor: str | None = None
    prazo_corrente: str | None = None
    prazo_intermediario: str | None = None
    destinacao_final: str | None = None
    pagina: int | None = None
    linha: int | None = None


@dataclass(frozen=True)
class TemporalidadeItem:
    """Item aprovado da tabela de temporalidade em estrutura mínima."""

    codigo: str
    descritor: str
    prazo_corrente: str | None = None
    prazo_intermediario: str | None = None
    destinacao_final: str | None = None
    observacao: str | None = None
    status_validacao: str = "aprovado"


@dataclass(frozen=True)
class RuleResult:
    """Resultado auditável de uma regra determinística."""

    rule_id: str
    rule_version: str
    field: str
    status: str
    led_value_original: str | None
    led_value_normalized: str
    expected_value: str | None
    message: str
    requires_human_validation: bool
    engine_version: str = RULE_ENGINE_VERSION
