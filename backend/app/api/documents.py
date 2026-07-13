"""Rotas para importação controlada de documentos originais."""

from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.schemas.document import StoredDocument
from app.services.file_validation import FileValidationError
from app.storage.local import get_stored_document, store_original_document

router = APIRouter(prefix="/documents", tags=["documentos"])


@router.post("", response_model=StoredDocument, status_code=status.HTTP_201_CREATED)
async def upload_document(
    document_kind: str = Form(description="Tipo: led ou tabela_temporalidade."),
    file: UploadFile = File(description="Arquivo PDF, CSV ou XLSX permitido para o MVP."),
) -> StoredDocument:
    """Recebe, valida, calcula hash e preserva o arquivo original."""

    content = await file.read()
    try:
        return store_original_document(
            content=content,
            original_filename=file.filename or "arquivo-sem-nome",
            content_type=file.content_type or "",
            document_kind=document_kind,
        )
    except FileValidationError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc


@router.get("/{document_id}", response_model=StoredDocument)
def read_document_metadata(document_id: str) -> StoredDocument:
    """Consulta metadados de um documento preservado."""

    document = get_stored_document(document_id)
    if document is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento não localizado.")
    return document
