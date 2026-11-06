---
name: aprovar-post
description: >
  Prepara um conteúdo já aprovado (blog + carrossel + legendas, criado por
  publicar-tema ou carrossel) para publicação, montando um pacote local
  pronto pra postar. Só publica direto numa rede social se já existir
  integração configurada (token válido) e o usuário autorizar
  explicitamente nesta execução. Nunca faz commit, push ou deploy — isso é
  sempre manual. Use quando o usuário disser "aprovar post X", "publicar
  o post do tema Y", "deixa esse conteúdo pronto pra postar", ou pedir pra
  finalizar a publicação de um conteúdo já criado.
---

# aprovar-post — Preparação e (opcional) publicação de conteúdo

Faz a ponte entre o conteúdo aprovado (blog + carrossel + legendas) e a
publicação real — mas a publicação de código (commit/push/deploy) é
**sempre manual**. Esta skill nunca roda `git push`, nunca configura
remoto e nunca depende de deploy automático.

## Quando usar

- Conteúdo (blog + carrossel + legendas) já criado por `publicar-tema`
  ou `carrossel` e aprovado internamente, pronto pra virar entrega final.

## Quando não usar

- Conteúdo ainda não foi criado → usar `publicar-tema` ou `carrossel`
  primeiro.
- Usuário ainda está revisando → não rodar até ele dizer "aprovado" /
  "pode postar".

## Entradas

- Slug do conteúdo (nome da pasta/arquivo, sem extensão). Se não vier,
  listar os conteúdos em rascunho (`draft: true` ou pasta mais recente em
  `workspaces/clientes/<cliente>/projetos/<projeto>/04-marketing/`) e perguntar qual.

## Dependências

- Blog: arquivo markdown do artigo (caminho depende de onde o projeto
  guarda o conteúdo — perguntar se não for óbvio).
- Carrossel: PNGs gerados pela skill `carrossel` na mesma pasta do
  conteúdo.
- Legendas: `legenda.md` e (se houver) `legenda-linkedin.md`.
- **Integração de publicação (opcional):** só existe se o usuário já
  configurou tokens de API (ex.: Meta Graph API) em `.env` **e** os
  scripts correspondentes já existem no projeto. Se não existir, a skill
  não tenta publicar nada sozinha.

## Contexto que deve ser carregado

- `_memoria/preferencias.md` (tom da mensagem de confirmação/checklist)
- Memória do cliente/projeto ativo, se aplicável

---

## Workflow

### Passo 1 — Localizar arquivos

- Blog (se houver): localizar o markdown do artigo.
- Carrossel: PNGs em `.../instagram/slide-01.png` até `slide-NN.png`.
- Validar que existem `legenda.md` e, se pedido, `legenda-linkedin.md`.

Se faltar qualquer peça esperada, parar e relatar o que falta — não
improvisar conteúdo ausente.

### Passo 2 — Mostrar resumo e pedir confirmação

Mostrar:
- Título do conteúdo
- Quantos slides do carrossel
- Primeiras linhas da legenda
- Se existe integração de publicação configurada (sim/não) e para quais
  canais

Perguntar: **"Confirma que esse conteúdo está pronto? (sim/não)"**. Só
seguir se a resposta for sim.

### Passo 3 — Montar o pacote local de publicação

Sempre fazer isso, com ou sem integração configurada. Criar:

```
<pasta-do-conteudo>/pacote-publicacao/
  blog.md              — versão final do artigo, já com draft: false
  instagram/           — PNGs do carrossel prontos
  legenda.md
  legenda-linkedin.md  — se existir
  CHECKLIST.md         — passo a passo manual de publicação
```

O artigo original (com `draft: true`) **não é alterado** — a versão
"pronta pra publicar" fica só dentro do pacote. Quem decide subir o blog
de verdade edita o arquivo original manualmente (ou pede pra fazer isso
como uma edição separada, fora desta skill).

`CHECKLIST.md` deve conter, adaptado ao que existe:

```markdown
# Checklist de publicação — <título>

- [ ] Revisar blog.md e colar/aplicar no site (flipar draft: false no
      arquivo real, ou colar no CMS)
- [ ] Rodar o deploy do site do jeito que o projeto usa (manual —
      esta skill não faz commit nem push)
- [ ] Conferir que o post está no ar antes de divulgar
- [ ] Subir os PNGs de instagram/ no Instagram + Facebook, usando
      legenda.md
- [ ] Colar legenda-linkedin.md no LinkedIn manualmente
```

### Passo 4 — Publicação direta (somente se aplicável)

Só executar este passo se **as duas condições** forem verdadeiras:

1. Integração de publicação já está configurada no projeto (token válido
   em `.env` + script de postagem já existe).
2. O usuário autorizou explicitamente **nesta execução** — perguntar:
   > "Tem integração configurada pra Instagram/Facebook. Quer que eu
   > poste agora mesmo, ou prefere só deixar o pacote pronto pra você
   > postar manualmente?"

Se o usuário disser sim: rodar o script de postagem existente (ex.:
`postar-instagram.js`, `postar-facebook.js`), capturar o link do post,
mostrar resultado. Se algum passo falhar, parar e relatar — não tentar
alternativa automática.

Se não houver integração configurada, ou o usuário preferir manual: parar
no Passo 3 e apresentar o pacote + checklist como entrega final.

### Passo 5 — Resumo

```
✓ Pacote de publicação pronto: <pasta>/pacote-publicacao/
  - blog.md (pronto pra aplicar no site)
  - instagram/ (PNGs prontos)
  - legenda.md / legenda-linkedin.md
  - CHECKLIST.md com os passos manuais

[Se publicou via integração:]
✓ Publicado agora:
  Instagram: <link>
  Facebook: <link>
```

## Tratamento de erro / rollback

- Se a montagem do pacote falhar no meio (ex.: PNG faltando), não deixar
  pacote parcial — apagar o que foi criado no `pacote-publicacao/` desta
  rodada e relatar o que faltou.
- Se a publicação via integração (Passo 4) falhar, relatar exatamente o
  que subiu e o que não subiu — nunca tentar "consertar" fazendo commit
  ou push.

## Saídas

Pacote de publicação local (`pacote-publicacao/`) com blog pronto,
PNGs, legendas e checklist manual — e, se autorizado, publicação direta
nas redes já configuradas.

## Critérios de qualidade

- O pacote nunca sai incompleto — se faltar peça, a skill para e relata
  em vez de entregar parcial.

## Regras

- **Nunca rodar `git add`, `git commit`, `git push` ou qualquer comando
  de deploy.** Publicação de código é sempre manual, fora desta skill —
  se o usuário quiser versionar o pacote, isso é `salvar-local` (que
  também nunca dá push sozinha).
- **Nunca configurar remoto nem depender de deploy automático
  (Netlify/Vercel/CI).**
- Postagem direta em rede social só com integração já configurada +
  confirmação explícita nesta execução — nunca por padrão.
- Confirmação humana antes de qualquer coisa (Passo 2) — não pular.
- Não inventar link de post ou status de publicação — só reportar o que
  de fato aconteceu.

## Critérios de validação

- Pacote de publicação criado só depois de confirmação do Passo 2.
- Nenhum comando de git executado por esta skill.
- Se integração não existir, a skill nunca tenta publicar sozinha.

## Limitações

- Não sabe fazer deploy de site — isso é sempre manual ou de outra
  ferramenta do usuário.
- Não cria os scripts de integração (`postar-instagram.js` etc.) — só os
  usa se já existirem.

## Caminho de salvamento

`<pasta-do-conteudo>/pacote-publicacao/`

## Contrato de handoff

Depois de gerar o pacote, encerra — não encadeia automaticamente com
`salvar-local` nem com nenhuma skill de deploy. Se o usuário quiser
registrar a sessão, ele pede `salvar-local` separadamente.

## Exemplos de gatilhos positivos

- "Aprovar post X"
- "Deixa esse conteúdo pronto pra postar"
- "Publica o post do tema Y" (já criado por `publicar-tema`)

## Exemplos de gatilhos negativos

- "Cria o carrossel desse tema" (conteúdo ainda não existe — é
  `carrossel`/`publicar-tema` primeiro)
- "Dá push nas alterações" (esta skill nunca faz isso — é `salvar-local`,
  que também nunca dá push sozinha)
