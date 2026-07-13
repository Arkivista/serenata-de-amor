"""Esquemas de entrada e saída para documentos armazenados.

Usa `dataclass` para manter os serviços centrais testáveis mesmo quando as
dependências web ainda não foram instaladas no ambiente local.
"""

from dataclasses import asdict, dataclass
from typing import Any


@dataclass(frozen=True)
class StoredDocument:
    """Metadados de um arquivo preservado no armazenamento local do MVP."""

    document_id: str
    original_filename: str
    stored_filename: str
    content_type: str
    size_bytes: int
    sha256: str
    document_kind: str
    status: str
    storage_path: str

    def model_dump(self) -> dict[str, Any]:
        """Compatibilidade simples com a nomenclatura do Pydantic."""

        return asdict(self)

    @classmethod
    def model_validate(cls, data: dict[str, Any]) -> "StoredDocument":
        """Recria metadados salvos, ignorando campos extras como `created_at`."""

        allowed = cls.__dataclass_fields__.keys()
        return cls(**{key: data[key] for key in allowed})
