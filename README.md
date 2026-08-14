# Currículo e papel timbrado — Brunoer Teles Barreto Filho

Identidade visual, currículo redesenhado e papel timbrado para uso em cartas de
apresentação e comunicações.

## Arquivos

| Arquivo | O que é |
|---|---|
| [`ANALISE-E-MELHORIAS.md`](ANALISE-E-MELHORIAS.md) | Diagnóstico do currículo original, o que foi corrigido e o que ainda depende de você |
| [`curriculo/curriculo-brunoer-teles-barreto-filho.pdf`](curriculo/) | Currículo final, uma página, pronto para enviar |
| [`curriculo/curriculo-brunoer-teles-barreto-filho.html`](curriculo/) | Fonte editável do currículo |
| [`timbrado/papel-timbrado.pdf`](timbrado/) | Papel timbrado em branco |
| [`timbrado/papel-timbrado.html`](timbrado/) | Fonte editável do timbrado (é aqui que se escreve a carta) |
| [`identidade/IDENTIDADE-VISUAL.md`](identidade/IDENTIDADE-VISUAL.md) | Cores, tipografia, filetes e margens, para manter tudo consistente |

## Como editar

Os arquivos `.html` são autossuficientes — abrem em qualquer navegador e se editam
em qualquer editor de texto. Para atualizar o conteúdo, altere o `.html` e gere o PDF
de novo.

## Como gerar os PDFs

Com o Chrome ou o Edge instalado, abra o `.html` no navegador e use
**Imprimir → Salvar como PDF**, com:

- papel **A4**;
- margens **Nenhuma** (as margens já estão no arquivo);
- **desmarcar** "Cabeçalhos e rodapés";
- **marcar** "Gráficos de plano de fundo" — sem isso o selo e os filetes somem.

Por linha de comando, com Chrome ou Chromium disponível:

```bash
./gerar-pdf.sh
```
