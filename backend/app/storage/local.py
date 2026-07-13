"""Armazenamento local preservando arquivos originais e metadados."""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from uuid import uuid4

from app.core.config import get_settings
from app.schemas.document import StoredDocument
from app.services.file_validation import (
    validate_content_type,
    validate_file_size,
    validate_filename_extension,
)


def _safe_suffix(filename: str) -> str:
    return Path(filename).suffix.lower()


def _sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


def store_original_document(
    *,
    content: bytes,
    original_filename: str,
    content_type: str,
    document_kind: str,
) -> StoredDocument:
    """Valida e preserva um arquivo original em armazenamento local.

    O arquivo original não é alterado. O nome em disco usa UUID para evitar
    colisão, caminho malicioso ou exposição desnecessária do nome original.
    """

    settings = get_settings()
    extension = validate_filename_extension(original_filename, document_kind)
    validate_content_type(extension, content_type)
    validate_file_size(len(content), settings.max_upload_size_mb)

    document_id = str(uuid4())
    digest = _sha256(content)
    stored_filename = f"{document_id}{_safe_suffix(original_filename)}"
    storage_root = Path(settings.storage_path)
    storage_root.mkdir(parents=True, exist_ok=True)
    file_path = storage_root / stored_filename
    metadata_path = storage_root / f"{document_id}.metadata.json"

    file_path.write_bytes(content)

    document = StoredDocument(
        document_id=document_id,
        original_filename=original_filename,
        stored_filename=stored_filename,
        content_type=content_type,
        size_bytes=len(content),
        sha256=digest,
        document_kind=document_kind,
        status="recebido_preservado_original",
        storage_path=str(file_path),
    )
    metadata = document.model_dump() | {"created_at": datetime.now(timezone.utc).isoformat()}
    metadata_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")
    return document


def get_stored_document(document_id: str) -> StoredDocument | None:
    """Consulta metadados de um documento preservado localmente."""

    metadata_path = Path(get_settings().storage_path) / f"{document_id}.metadata.json"
    if not metadata_path.exists():
        return None
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    return StoredDocument.model_validate(metadata)
