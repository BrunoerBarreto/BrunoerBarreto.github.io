# turbo-carnival — Organizador de Arquivos

Ferramenta de linha de comando em Python que organiza automaticamente arquivos
e documentos: classifica por tipo, assunto e data, cria as pastas necessárias,
detecta duplicados, renomeia os arquivos de forma clara e gera um relatório da
organização.

Funciona bem com PDFs, documentos Word, planilhas, imagens e arquivos de
texto — e qualquer outro tipo de arquivo é organizado em uma categoria
"Outros".

## Como funciona

Para cada arquivo encontrado (recursivamente) na pasta de origem:

1. **Classificação por tipo** — a extensão define a categoria (`Documentos`,
   `Planilhas`, `Apresentacoes`, `Imagens`, `Textos` ou `Outros`).
2. **Assunto** — extraído dos metadados do documento (título do PDF/Word/
   Excel) quando disponível; caso contrário, derivado do nome do arquivo
   (remove datas, números e palavras comuns como "de", "final", "cópia").
3. **Data** — a data de modificação do arquivo, usada para organizar em
   subpastas `AAAA-MM`.
4. **Duplicados** — arquivos com conteúdo idêntico (hash SHA-256) são
   movidos para uma pasta `Duplicados/`, mantendo apenas um exemplar
   organizado normalmente.
5. **Renomeação** — o nome final é `AAAA-MM-DD_nome-limpo.ext`, sem acentos
   ou espaços, com sufixo numérico automático em caso de colisão de nomes.
6. **Relatório** — um resumo com totais, contagem por categoria, duplicados
   e eventuais erros é exibido no terminal e pode ser salvo em arquivo.

A estrutura final fica assim:

```
destino/
├── Documentos/
│   └── Contrato/2024-03/2024-03-15_contrato-aluguel.pdf
├── Planilhas/
│   └── Vendas/2024-01/2024-01-10_vendas-janeiro.xlsx
├── Imagens/
│   └── Geral/2023-12/2023-12-25_foto.jpg
└── Duplicados/
    └── copia-do-contrato.pdf
```

## Instalação

Requer Python 3.9+.

```bash
pip install -e ".[dev]"
```

Para tentar extrair o título de PDFs, DOCX e XLSX como assunto (opcional):

```bash
pip install -e ".[metadados]"
```

Sem essa dependência extra, o assunto é sempre derivado do nome do arquivo —
a ferramenta funciona normalmente.

## Uso

```bash
# Simular a organização antes de mexer em qualquer arquivo (recomendado)
organizador --origem ~/Downloads --destino ~/Organizado --dry-run

# Organizar de fato, movendo os arquivos
organizador --origem ~/Downloads --destino ~/Organizado

# Copiar em vez de mover (mantém os arquivos originais)
organizador --origem ~/Downloads --destino ~/Organizado --copiar

# Salvar o relatório em um arquivo
organizador --origem ~/Downloads --destino ~/Organizado --relatorio relatorio.txt
```

| Opção         | Descrição                                             |
| ------------- | ------------------------------------------------------ |
| `--origem`    | Pasta com os arquivos a organizar (obrigatório)         |
| `--destino`   | Pasta onde os arquivos organizados serão colocados (obrigatório) |
| `--copiar`    | Copia os arquivos em vez de movê-los                    |
| `--dry-run`   | Simula a organização sem mover/copiar nada               |
| `--relatorio` | Caminho para salvar o relatório em texto                 |

## Testes

```bash
pytest
```

Os testes cobrem cada módulo isoladamente (classificação, duplicados,
renomeação, metadados, relatório) e a orquestração de ponta a ponta
(`Organizador`), além da CLI.

## Limitações conhecidas

- Em modo `--dry-run`, a checagem de nomes duplicados no destino não detecta
  colisões entre dois arquivos simulados na mesma execução, já que nenhuma
  pasta é criada de fato.
- A extração de "assunto" pelos metadados é melhor-esforço: documentos sem
  título definido caem automaticamente no nome do arquivo.
