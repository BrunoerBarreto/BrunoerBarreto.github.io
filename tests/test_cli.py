from organizador.cli import main


def test_cli_organiza_arquivos(tmp_path, capsys):
    origem = tmp_path / "origem"
    origem.mkdir()
    (origem / "nota.txt").write_text("conteudo", encoding="utf-8")
    destino = tmp_path / "destino"

    codigo = main(["--origem", str(origem), "--destino", str(destino)])

    saida = capsys.readouterr().out
    assert codigo == 0
    assert "Total de arquivos processados: 1" in saida
    assert list(destino.rglob("*.txt"))


def test_cli_falha_com_origem_inexistente(tmp_path, capsys):
    codigo = main(["--origem", str(tmp_path / "nao_existe"), "--destino", str(tmp_path / "destino")])
    erro = capsys.readouterr().err

    assert codigo == 1
    assert "não encontrada" in erro


def test_cli_salva_relatorio_em_arquivo(tmp_path):
    origem = tmp_path / "origem"
    origem.mkdir()
    (origem / "nota.txt").write_text("conteudo", encoding="utf-8")
    destino = tmp_path / "destino"
    relatorio_path = tmp_path / "relatorio.txt"

    main(["--origem", str(origem), "--destino", str(destino), "--relatorio", str(relatorio_path)])

    assert relatorio_path.exists()


def test_cli_dry_run_nao_move_arquivos(tmp_path):
    origem = tmp_path / "origem"
    origem.mkdir()
    arquivo = origem / "nota.txt"
    arquivo.write_text("conteudo", encoding="utf-8")
    destino = tmp_path / "destino"

    main(["--origem", str(origem), "--destino", str(destino), "--dry-run"])

    assert arquivo.exists()
