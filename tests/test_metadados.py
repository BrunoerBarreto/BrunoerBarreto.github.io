from datetime import datetime

from organizador.metadados import obter_assunto, obter_data


def test_obter_data_usa_data_de_modificacao(tmp_path, criar_arquivo):
    arquivo = criar_arquivo(tmp_path / "nota.txt")
    assert isinstance(obter_data(arquivo), datetime)


def test_obter_assunto_ignora_datas_e_numeros_no_nome(tmp_path, criar_arquivo):
    arquivo = criar_arquivo(tmp_path / "contrato_2024_001.txt")
    assert obter_assunto(arquivo) == "Contrato"


def test_obter_assunto_ignora_palavras_comuns(tmp_path, criar_arquivo):
    arquivo = criar_arquivo(tmp_path / "relatorio_de_vendas_final.txt")
    assunto = obter_assunto(arquivo)
    assert "De" not in assunto.split()
    assert "Final" not in assunto.split()


def test_obter_assunto_nome_so_com_numeros_retorna_geral(tmp_path, criar_arquivo):
    arquivo = criar_arquivo(tmp_path / "20240315.txt")
    assert obter_assunto(arquivo) == "Geral"
