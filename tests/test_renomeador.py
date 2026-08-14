from datetime import datetime
from pathlib import Path

from organizador.renomeador import gerar_caminho_unico, gerar_novo_nome, limpar_nome


def test_limpar_nome_remove_acentos_e_espacos():
    assert limpar_nome("Relatório Final 2024") == "relatorio-final-2024"


def test_limpar_nome_remove_simbolos():
    assert limpar_nome("nota!!fiscal@@2024") == "nota-fiscal-2024"


def test_limpar_nome_vazio_retorna_arquivo_padrao():
    assert limpar_nome("---") == "arquivo"


def test_gerar_novo_nome_inclui_data_e_extensao():
    data = datetime(2024, 3, 15)
    nome = gerar_novo_nome(Path("Relatório Financeiro.pdf"), data)
    assert nome == "2024-03-15_relatorio-financeiro.pdf"


def test_gerar_caminho_unico_sem_colisao(tmp_path):
    destino = gerar_caminho_unico(tmp_path, "arquivo.txt")
    assert destino == tmp_path / "arquivo.txt"


def test_gerar_caminho_unico_com_colisao_adiciona_contador(tmp_path):
    (tmp_path / "arquivo.txt").write_text("existente")
    destino = gerar_caminho_unico(tmp_path, "arquivo.txt")
    assert destino == tmp_path / "arquivo_1.txt"


def test_gerar_caminho_unico_com_multiplas_colisoes(tmp_path):
    (tmp_path / "arquivo.txt").write_text("a")
    (tmp_path / "arquivo_1.txt").write_text("b")
    destino = gerar_caminho_unico(tmp_path, "arquivo.txt")
    assert destino == tmp_path / "arquivo_2.txt"
