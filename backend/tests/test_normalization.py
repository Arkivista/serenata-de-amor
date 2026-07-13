from app.normalization.code import normalize_code
from app.normalization.text import normalize_for_comparison, normalize_whitespace


def test_normalize_whitespace_preserves_original_value():
    result = normalize_whitespace("  Controle   de frequência  ")

    assert result.original == "  Controle   de frequência  "
    assert result.normalized == "Controle de frequência"


def test_text_comparison_normalization_removes_case_and_accents():
    result = normalize_for_comparison("CONTROLE DE FREQUÊNCIA")

    assert result.normalized == "controle de frequencia"


def test_code_normalization_preserves_dots_and_zeroes():
    result = normalize_code(" 023.15 ")

    assert result.normalized == "023.15"
