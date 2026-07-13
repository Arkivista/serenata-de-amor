from pathlib import Path

from app.storage.local import get_stored_document, store_original_document


def test_store_original_document_preserves_content_and_metadata(monkeypatch, tmp_path):
    monkeypatch.setenv("LED_STORAGE_PATH", str(tmp_path))

    document = store_original_document(
        content=b"%PDF-1.4 conteudo ficticio para teste",
        original_filename="LED Exemplo.pdf",
        content_type="application/pdf",
        document_kind="led",
    )

    stored_path = Path(document.storage_path)
    assert stored_path.exists()
    assert stored_path.read_bytes() == b"%PDF-1.4 conteudo ficticio para teste"
    assert document.original_filename == "LED Exemplo.pdf"
    assert document.stored_filename.endswith(".pdf")
    assert document.status == "recebido_preservado_original"

    reloaded = get_stored_document(document.document_id)
    assert reloaded == document
