"""Coleta de resultados e geração do relatório final da organização."""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from .modelos import ResultadoArquivo


class Relatorio:
    """Coleta os resultados do processamento e gera um resumo legível."""

    def __init__(self) -> None:
        self.itens: list[ResultadoArquivo] = []

    def adicionar(self, item: ResultadoArquivo) -> None:
        self.itens.append(item)

    @property
    def total(self) -> int:
        return len(self.itens)

    @property
    def duplicados(self) -> list[ResultadoArquivo]:
        return [item for item in self.itens if item.duplicado_de is not None]

    @property
    def erros(self) -> list[ResultadoArquivo]:
        return [item for item in self.itens if item.erro is not None]

    @property
    def organizados(self) -> list[ResultadoArquivo]:
        return [item for item in self.itens if item.erro is None and item.duplicado_de is None]

    def por_categoria(self) -> Counter:
        return Counter(item.categoria for item in self.organizados)

    def gerar_texto(self) -> str:
        linhas = [
            "Relatório de Organização",
            "=" * 25,
            f"Total de arquivos processados: {self.total}",
            f"Organizados: {len(self.organizados)}",
            f"Duplicados encontrados: {len(self.duplicados)}",
            f"Erros: {len(self.erros)}",
            "",
            "Por categoria:",
        ]
        for categoria, quantidade in sorted(self.por_categoria().items()):
            linhas.append(f"  {categoria}: {quantidade}")

        if self.duplicados:
            linhas += ["", "Duplicados:"]
            for item in self.duplicados:
                linhas.append(f"  {item.origem} (igual a {item.duplicado_de})")

        if self.erros:
            linhas += ["", "Erros:"]
            for item in self.erros:
                linhas.append(f"  {item.origem}: {item.erro}")

        return "\n".join(linhas)

    def salvar(self, caminho: Path) -> None:
        caminho.write_text(self.gerar_texto(), encoding="utf-8")
