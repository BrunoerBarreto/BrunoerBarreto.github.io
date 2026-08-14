"""Interface de linha de comando do organizador."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .organizador import Organizador


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="organizador",
        description="Organiza automaticamente arquivos e documentos por tipo, assunto e data.",
    )
    parser.add_argument("--origem", required=True, type=Path, help="Pasta com os arquivos a organizar")
    parser.add_argument(
        "--destino", required=True, type=Path, help="Pasta onde os arquivos organizados serão colocados"
    )
    parser.add_argument("--copiar", action="store_true", help="Copia os arquivos em vez de movê-los")
    parser.add_argument(
        "--dry-run", action="store_true", help="Simula a organização sem mover ou copiar nenhum arquivo"
    )
    parser.add_argument(
        "--relatorio", type=Path, default=None, help="Caminho para salvar o relatório em um arquivo de texto"
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = criar_parser()
    args = parser.parse_args(argv)

    if not args.origem.is_dir():
        print(f"Erro: pasta de origem não encontrada: {args.origem}", file=sys.stderr)
        return 1

    organizador = Organizador(
        origem=args.origem,
        destino=args.destino,
        copiar=args.copiar,
        dry_run=args.dry_run,
    )
    relatorio = organizador.executar()

    print(relatorio.gerar_texto())

    if args.relatorio:
        relatorio.salvar(args.relatorio)
        print(f"\nRelatório salvo em: {args.relatorio}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
