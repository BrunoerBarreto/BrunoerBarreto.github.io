"""Detecção de arquivos duplicados por hash de conteúdo."""

from __future__ import annotations

import hashlib
from collections import defaultdict
from pathlib import Path

_TAMANHO_BLOCO = 65536


def calcular_hash(caminho: Path) -> str:
    """Calcula o hash SHA-256 do conteúdo do arquivo."""
    sha256 = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(_TAMANHO_BLOCO), b""):
            sha256.update(bloco)
    return sha256.hexdigest()


def agrupar_por_conteudo(arquivos: list[Path]) -> dict[str, list[Path]]:
    """Agrupa arquivos pelo hash do conteúdo."""
    grupos: dict[str, list[Path]] = defaultdict(list)
    for arquivo in arquivos:
        grupos[calcular_hash(arquivo)].append(arquivo)
    return grupos


def encontrar_duplicados(arquivos: list[Path]) -> dict[str, list[Path]]:
    """Retorna apenas os grupos com conteúdo idêntico (mais de um arquivo)."""
    grupos = agrupar_por_conteudo(arquivos)
    return {hash_: arquivos_ for hash_, arquivos_ in grupos.items() if len(arquivos_) > 1}
