"""Validação determinística de arquivos recebidos pelo MVP."""

from pathlib import Path

ALLOWED_EXTENSIONS_BY_KIND = {
    "led": {".pdf"},
    "tabela_temporalidade": {".pdf", ".csv", ".xlsx"},
}

ALLOWED_CONTENT_TYPES_BY_EXTENSION = {
    ".pdf": {"application/pdf"},
    ".csv": {"text/csv", "application/csv", "application/vnd.ms-excel"},
    ".xlsx": {"application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"},
}


class FileValidationError(ValueError):
    """Erro de validação de arquivo explicado ao usuário."""


def validate_document_kind(document_kind: str) -> None:
    """Valida o tipo documental declarado pelo usuário."""

    if document_kind not in ALLOWED_EXTENSIONS_BY_KIND:
        allowed = ", ".join(sorted(ALLOWED_EXTENSIONS_BY_KIND))
        raise FileValidationError(f"Tipo de documento inválido. Use um destes valores: {allowed}.")


def validate_filename_extension(filename: str, document_kind: str) -> str:
    """Valida a extensão conforme o tipo documental informado."""

    validate_document_kind(document_kind)
    extension = Path(filename).suffix.lower()
    allowed = ALLOWED_EXTENSIONS_BY_KIND[document_kind]
    if extension not in allowed:
        allowed_text = ", ".join(sorted(allowed))
        raise FileValidationError(
            f"Extensão inválida para {document_kind}. Extensões permitidas: {allowed_text}."
        )
    return extension


def validate_content_type(extension: str, content_type: str) -> None:
    """Valida o MIME type informado no upload."""

    allowed = ALLOWED_CONTENT_TYPES_BY_EXTENSION[extension]
    normalized_content_type = (content_type or "").split(";")[0].strip().lower()
    if normalized_content_type not in allowed:
        allowed_text = ", ".join(sorted(allowed))
        raise FileValidationError(
            f"MIME type inválido para {extension}. Esperado: {allowed_text}. Recebido: {content_type or 'não informado'}."
        )


def validate_file_size(size_bytes: int, max_upload_size_mb: int) -> None:
    """Valida o tamanho máximo permitido para upload."""

    max_bytes = max_upload_size_mb * 1024 * 1024
    if size_bytes <= 0:
        raise FileValidationError("Arquivo vazio não pode ser importado.")
    if size_bytes > max_bytes:
        raise FileValidationError(
            f"Arquivo excede o limite de {max_upload_size_mb} MB definido para o MVP."
        )
