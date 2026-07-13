import pytest

from app.services.file_validation import (
    FileValidationError,
    validate_content_type,
    validate_file_size,
    validate_filename_extension,
)


def test_led_accepts_only_pdf_extension():
    assert validate_filename_extension("led.pdf", "led") == ".pdf"


@pytest.mark.parametrize("filename", ["led.csv", "led.xlsx", "led.txt"])
def test_led_rejects_non_pdf_extensions(filename):
    with pytest.raises(FileValidationError):
        validate_filename_extension(filename, "led")


def test_temporalidade_accepts_pdf_csv_and_xlsx():
    assert validate_filename_extension("tabela.pdf", "tabela_temporalidade") == ".pdf"
    assert validate_filename_extension("tabela.csv", "tabela_temporalidade") == ".csv"
    assert validate_filename_extension("tabela.xlsx", "tabela_temporalidade") == ".xlsx"


def test_rejects_unexpected_content_type():
    with pytest.raises(FileValidationError):
        validate_content_type(".pdf", "text/plain")


def test_rejects_empty_file():
    with pytest.raises(FileValidationError):
        validate_file_size(0, 50)
