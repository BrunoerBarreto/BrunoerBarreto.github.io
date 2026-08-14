from pathlib import Path

from organizador.classificador import classificar_por_tipo


def test_classifica_documento_pdf():
    assert classificar_por_tipo(Path("relatorio.pdf")) == "Documentos"


def test_classifica_planilha_xlsx():
    assert classificar_por_tipo(Path("vendas.xlsx")) == "Planilhas"


def test_classifica_imagem_png():
    assert classificar_por_tipo(Path("foto.png")) == "Imagens"


def test_classifica_texto_txt():
    assert classificar_por_tipo(Path("notas.txt")) == "Textos"


def test_extensao_desconhecida_vai_para_outros():
    assert classificar_por_tipo(Path("dados.xyz")) == "Outros"


def test_extensao_maiuscula_e_reconhecida():
    assert classificar_por_tipo(Path("FOTO.PNG")) == "Imagens"
