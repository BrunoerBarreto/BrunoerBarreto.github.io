"""Classificação de arquivos por tipo/categoria com base na extensão."""

from __future__ import annotations

from pathlib import Path

CATEGORIAS: dict[str, set[str]] = {
    "Documentos": {".pdf", ".doc", ".docx", ".odt", ".rtf"},
    "Planilhas": {".xls", ".xlsx", ".csv", ".ods"},
    "Apresentacoes": {".ppt", ".pptx", ".odp"},
    "Imagens": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"},
    "Textos": {".txt", ".md"},
}

CATEGORIA_OUTROS = "Outros"


def classificar_por_tipo(caminho: Path) -> str:
    """Retorna a categoria do arquivo com base em sua extensão."""
    extensao = caminho.suffix.lower()
    for categoria, extensoes in CATEGORIAS.items():
        if extensao in extensoes:
            return categoria
    return CATEGORIA_OUTROS
