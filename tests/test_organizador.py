from organizador.organizador import Organizador


def test_organiza_arquivos_por_categoria(pasta_origem, pasta_destino, criar_arquivo):
    criar_arquivo(pasta_origem / "relatorio.pdf", "conteudo pdf")
    criar_arquivo(pasta_origem / "foto.png", "conteudo imagem")

    relatorio = Organizador(pasta_origem, pasta_destino).executar()

    assert relatorio.total == 2
    assert len(relatorio.organizados) == 2
    arquivos_destino = [p for p in pasta_destino.rglob("*") if p.is_file()]
    assert any(p.suffix == ".pdf" for p in arquivos_destino)
    assert any(p.suffix == ".png" for p in arquivos_destino)


def test_move_arquivos_por_padrao(pasta_origem, pasta_destino, criar_arquivo):
    arquivo = criar_arquivo(pasta_origem / "nota.txt", "texto")

    Organizador(pasta_origem, pasta_destino).executar()

    assert not arquivo.exists()


def test_copiar_mantem_arquivo_original(pasta_origem, pasta_destino, criar_arquivo):
    arquivo = criar_arquivo(pasta_origem / "nota.txt", "texto")

    Organizador(pasta_origem, pasta_destino, copiar=True).executar()

    assert arquivo.exists()


def test_dry_run_nao_altera_nada(pasta_origem, pasta_destino, criar_arquivo):
    arquivo = criar_arquivo(pasta_origem / "nota.txt", "texto")

    relatorio = Organizador(pasta_origem, pasta_destino, dry_run=True).executar()

    assert arquivo.exists()
    assert not pasta_destino.exists()
    assert relatorio.total == 1


def test_detecta_e_isola_duplicados(pasta_origem, pasta_destino, criar_arquivo):
    criar_arquivo(pasta_origem / "original.txt", "mesmo conteudo")
    criar_arquivo(pasta_origem / "copia.txt", "mesmo conteudo")

    relatorio = Organizador(pasta_origem, pasta_destino).executar()

    assert len(relatorio.organizados) == 1
    assert len(relatorio.duplicados) == 1

    pasta_duplicados = pasta_destino / "Duplicados"
    assert pasta_duplicados.exists()
    assert len(list(pasta_duplicados.iterdir())) == 1


def test_subpastas_da_origem_sao_percorridas(pasta_origem, pasta_destino, criar_arquivo):
    criar_arquivo(pasta_origem / "sub" / "documento.pdf", "conteudo")

    relatorio = Organizador(pasta_origem, pasta_destino).executar()

    assert relatorio.total == 1
    assert len(relatorio.organizados) == 1
