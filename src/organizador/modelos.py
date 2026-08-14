"""Estruturas de dados usadas em todo o pacote."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class ResultadoArquivo:
    """Resultado do processamento de um único arquivo."""

    origem: Path
    categoria: str
    destino: Path | None = None
    assunto: str | None = None
    duplicado_de: Path | None = None
    erro: str | None = None
