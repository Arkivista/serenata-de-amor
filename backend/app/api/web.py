"""Tela web simples para testar o protótipo sem comandos curl."""

from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter(tags=["protótipo web"])


@router.get("/", response_class=HTMLResponse)
def prototype_home() -> HTMLResponse:
    """Exibe uma página simples de teste da análise estruturada."""

    html_path = Path(__file__).resolve().parents[1] / "web" / "index.html"
    return HTMLResponse(html_path.read_text(encoding="utf-8"))
