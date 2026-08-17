# Brunoer Barreto Advocacia — Site Institucional

Site institucional em HTML/CSS/JS puro (sem build, sem dependências pagas), pronto para publicação gratuita no **GitHub Pages**.

Sociedade Individual de Advocacia com atuação em Direito Administrativo, licitações e contratos públicos (Lei nº 14.133/2021) e processos perante o Tribunal de Contas dos Municípios de Goiás (TCM-GO).

## 🌐 Endereço do site (domínio gratuito) — já está no ar

```
https://brunoerbarreto.github.io/
```

Esse endereço:

- **é gratuito para sempre**, sem custo de domínio ou hospedagem;
- **só pode ser alterado por quem tem acesso de escrita a este repositório GitHub** (você e quem você convidar) — qualquer outra pessoa apenas visualiza;
- fica acessível 24h, de qualquer dispositivo, sem precisar reinstalar nada;
- é o endereço **raiz** (sem nenhum sufixo depois de `.io/`) porque o repositório se chama exatamente `BrunoerBarreto.github.io` — esse é o nome especial que o GitHub reconhece para publicar no domínio principal do usuário.

O GitHub Pages está configurado no modo **"Deploy from a branch"**: qualquer `push` na branch `main` publica o site automaticamente em 1–2 minutos, sem precisar de nenhum workflow adicional. Acompanhe em Settings → Pages ou na aba **Actions** (evento "pages build and deployment").

Se um dia você registrar um domínio próprio — o ideal para um escritório é um `.adv.br`, exclusivo para advogados via Registro.br/OAB — basta apontar o DNS para o GitHub Pages e adicionar um arquivo `CNAME` neste repositório. O site continua exatamente o mesmo.

## ✏️ O que ainda falta personalizar

O conteúdo (textos, áreas de atuação, TCM-GO, FAQ, contato) já está preenchido com os dados reais do escritório. Falta apenas:

1. **Logo oficial** — `assets/logo.svg` é um ícone de balança dourada recriado a partir da descrição do briefing (gradiente dourado sobre grafite). Substitua pelo ícone/lockup real extraído do `Cartão_de_Visitas.pdf` assim que o arquivo puder ser enviado neste chat (anexado ou colado como imagem). Mesmo nome de arquivo (`assets/logo.svg`) evita precisar tocar no HTML.
2. **Respostas do FAQ** — foram redigidas como rascunho profissional a partir das 5 perguntas do briefing; revise o texto e ajuste conforme a prática real do escritório (prazos, política de honorários etc.).
3. Campos propositalmente **omitidos** por instrução do escritório: cidade/sede, endereço, código de atividade (CNAE) e data de abertura/porte da empresa — não foram incluídos em nenhum lugar do site.
4. **Instagram** — @brunoerbarretoadvocacia já está linkado no Contato, no rodapé e no `sameAs` do schema.org (SEO); é só o perfil ficar pronto.

## 📁 Estrutura

```
index.html      → estrutura e conteúdo do site (Início, Áreas de Atuação, TCM-GO, Como Funciona, Diferenciais, Sobre, FAQ, Contato)
style.css       → estilos (paleta grafite/dourado, tipografia Cinzel + IBM Plex, responsivo)
script.js       → menu mobile e ano dinâmico no rodapé
assets/         → logo (SVG)
```

A seção "Assessoria Jurídica Integral" usa `<details>/<summary>` nativos do HTML (sem JavaScript extra) para organizar 10 grupos temáticos em acordeão — mantém a página leve, acessível por teclado e compatível com `prefers-reduced-motion`.

## 💡 Sugestões para deixar o site mais completo (próximos passos)

- [ ] Substituir `assets/logo.svg` pela arte oficial extraída do Cartão de Visitas
- [ ] Revisar o texto do FAQ com as respostas definitivas do escritório
- [ ] Adicionar depoimentos reais de clientes/gestores atendidos (com autorização)
- [ ] Registrar um domínio `.adv.br` (Registro.br, exclusivo para advogados) e apontar para o GitHub Pages
- [ ] Adicionar política de privacidade / aviso LGPD, já que o site capta contatos por WhatsApp e e-mail
- [ ] Configurar Google Analytics ou Plausible para acompanhar visitas
- [ ] Testar em celular real antes de divulgar amplamente
- [ ] Divulgar o link em assinatura de e-mail, cartão de visitas e perfis profissionais (LinkedIn, etc.)
