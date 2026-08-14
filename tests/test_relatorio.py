from pathlib import Path

from organizador.modelos import ResultadoArquivo
from organizador.relatorio import Relatorio


def test_relatorio_vazio():
    relatorio = Relatorio()
    assert relatorio.total == 0
    assert "Total de arquivos processados: 0" in relatorio.gerar_texto()


def test_relatorio_conta_organizados_duplicados_e_erros():
    relatorio = Relatorio()
    relatorio.adicionar(
        ResultadoArquivo(origem=Path("a.pdf"), categoria="Documentos", destino=Path("dest/a.pdf"))
    )
    relatorio.adicionar(
        ResultadoArquivo(
            origem=Path("b.pdf"),
            categoria="Documentos",
            destino=Path("dest/b.pdf"),
            duplicado_de=Path("a.pdf"),
        )
    )
    relatorio.adicionar(
        ResultadoArquivo(origem=Path("c.pdf"), categoria="Documentos", erro="permissão negada")
    )

    assert relatorio.total == 3
    assert len(relatorio.organizados) == 1
    assert len(relatorio.duplicados) == 1
    assert len(relatorio.erros) == 1


def test_por_categoria_conta_apenas_organizados():
    relatorio = Relatorio()
    relatorio.adicionar(
        ResultadoArquivo(origem=Path("a.pdf"), categoria="Documentos", destino=Path("dest/a.pdf"))
    )
    relatorio.adicionar(
        ResultadoArquivo(origem=Path("b.png"), categoria="Imagens", destino=Path("dest/b.png"))
    )
    relatorio.adicionar(
        ResultadoArquivo(
            origem=Path("c.pdf"), categoria="Documentos", duplicado_de=Path("a.pdf")
        )
    )

    contagem = relatorio.por_categoria()
    assert contagem["Documentos"] == 1
    assert contagem["Imagens"] == 1


def test_salvar_relatorio_em_arquivo(tmp_path):
    relatorio = Relatorio()
    relatorio.adicionar(
        ResultadoArquivo(origem=Path("a.pdf"), categoria="Documentos", destino=Path("dest/a.pdf"))
    )
    caminho = tmp_path / "relatorio.txt"

    relatorio.salvar(caminho)

    assert caminho.exists()
    assert "Total de arquivos processados: 1" in caminho.read_text(encoding="utf-8")
