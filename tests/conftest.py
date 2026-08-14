from __future__ import annotations

from pathlib import Path

import pytest


@pytest.fixture
def pasta_origem(tmp_path: Path) -> Path:
    origem = tmp_path / "origem"
    origem.mkdir()
    return origem


@pytest.fixture
def pasta_destino(tmp_path: Path) -> Path:
    return tmp_path / "destino"


@pytest.fixture
def criar_arquivo():
    def _criar(caminho: Path, conteudo: str = "conteudo") -> Path:
        caminho.parent.mkdir(parents=True, exist_ok=True)
        caminho.write_text(conteudo, encoding="utf-8")
        return caminho

    return _criar
