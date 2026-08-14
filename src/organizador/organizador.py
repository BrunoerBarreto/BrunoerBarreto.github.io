"""Orquestração: percorre a origem e organiza os arquivos no destino."""

from __future__ import annotations

import shutil
from pathlib import Path

from .classificador import classificar_por_tipo
from .duplicados import encontrar_duplicados
from .metadados import obter_assunto, obter_data
from .modelos import ResultadoArquivo
from .relatorio import Relatorio
from .renomeador import gerar_caminho_unico, gerar_novo_nome

PASTA_DUPLICADOS = "Duplicados"


class Organizador:
    """Organiza arquivos de uma pasta de origem em uma pasta de destino."""

    def __init__(
        self,
        origem: Path,
        destino: Path,
        copiar: bool = False,
        dry_run: bool = False,
    ) -> None:
        self.origem = origem
        self.destino = destino
        self.copiar = copiar
        self.dry_run = dry_run

    def _listar_arquivos(self) -> list[Path]:
        return [caminho for caminho in self.origem.rglob("*") if caminho.is_file()]

    def _transferir(self, origem: Path, destino: Path) -> None:
        if self.dry_run:
            return
        destino.parent.mkdir(parents=True, exist_ok=True)
        if self.copiar:
            shutil.copy2(origem, destino)
        else:
            shutil.move(str(origem), str(destino))

    def _mapear_duplicados(self, arquivos: list[Path]) -> dict[Path, Path]:
        """Para cada arquivo repetido, indica qual é o arquivo "original" do grupo."""
        arquivo_original: dict[Path, Path] = {}
        for grupo in encontrar_duplicados(arquivos).values():
            principal, *repetidos = sorted(grupo)
            for repetido in repetidos:
                arquivo_original[repetido] = principal
        return arquivo_original

    def executar(self) -> Relatorio:
        relatorio = Relatorio()
        arquivos = self._listar_arquivos()
        arquivo_original = self._mapear_duplicados(arquivos)

        for arquivo in arquivos:
            try:
                categoria = classificar_por_tipo(arquivo)

                if arquivo in arquivo_original:
                    destino_final = gerar_caminho_unico(self.destino / PASTA_DUPLICADOS, arquivo.name)
                    self._transferir(arquivo, destino_final)
                    relatorio.adicionar(
                        ResultadoArquivo(
                            origem=arquivo,
                            categoria=categoria,
                            destino=destino_final,
                            duplicado_de=arquivo_original[arquivo],
                        )
                    )
                    continue

                data = obter_data(arquivo)
                assunto = obter_assunto(arquivo)
                pasta_destino = self.destino / categoria / assunto / data.strftime("%Y-%m")
                novo_nome = gerar_novo_nome(arquivo, data)
                destino_final = gerar_caminho_unico(pasta_destino, novo_nome)

                self._transferir(arquivo, destino_final)
                relatorio.adicionar(
                    ResultadoArquivo(
                        origem=arquivo,
                        categoria=categoria,
                        destino=destino_final,
                        assunto=assunto,
                    )
                )
            except Exception as erro:
                relatorio.adicionar(
                    ResultadoArquivo(origem=arquivo, categoria="Desconhecida", erro=str(erro))
                )

        return relatorio
