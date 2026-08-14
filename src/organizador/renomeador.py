"""Geração de nomes de arquivo limpos e únicos."""

from __future__ import annotations

import re
import unicodedata
from datetime import datetime
from pathlib import Path

_CARACTERES_INVALIDOS = re.compile(r"[^a-z0-9]+")


def limpar_nome(nome: str) -> str:
    """Normaliza um nome: remove acentos e símbolos, usa hífen como separador."""
    sem_acentos = unicodedata.normalize("NFKD", nome).encode("ascii", "ignore").decode()
    limpo = _CARACTERES_INVALIDOS.sub("-", sem_acentos.lower()).strip("-")
    return limpo or "arquivo"


def gerar_novo_nome(caminho: Path, data: datetime) -> str:
    """Gera um novo nome de arquivo com prefixo de data e nome limpo."""
    prefixo = data.strftime("%Y-%m-%d")
    nome_limpo = limpar_nome(caminho.stem)
    return f"{prefixo}_{nome_limpo}{caminho.suffix.lower()}"


def gerar_caminho_unico(pasta_destino: Path, nome_arquivo: str) -> Path:
    """Garante um caminho de destino sem colisão, adicionando um contador se necessário."""
    destino = pasta_destino / nome_arquivo
    if not destino.exists():
        return destino

    base = Path(nome_arquivo).stem
    extensao = Path(nome_arquivo).suffix
    contador = 1
    while True:
        candidato = pasta_destino / f"{base}_{contador}{extensao}"
        if not candidato.exists():
            return candidato
        contador += 1
