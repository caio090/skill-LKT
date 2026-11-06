---
name: estruturar-pagina-de-oferta
description: >
  Estrutura uma página de oferta/venda — headline, promessa, público,
  dor, oferta, prova, demonstração, expert (quando existir), CTA, FAQ,
  garantia, checkout e evento de conversão associado. Nunca presume que
  toda empresa tem um expert pessoal. Use quando o usuário disser
  "preciso de uma página de venda", "monta a landing page da oferta X".
---

# estruturar-pagina-de-oferta — Da promessa ao evento de conversão

Estrutura o conteúdo de uma página de oferta, distinguindo imagem do
expert, VSL, demonstração e prova social (ver
`knowledge/marketing/EXPERT_E_PAGINA_DE_OFERTA.md`), sempre encadeando
com `pagina-e-site` e `design-front-end` para a implementação visual.

## Quando usar

- A entrega inclui uma página cujo objetivo é converter (venda,
  cadastro, agendamento).

## Quando não usar

- Para página institucional sem objetivo de conversão direto (isso é
  `pagina-e-site` sem esta skill).

## Entradas

- Público e dor que a oferta resolve.
- O que é a oferta, o que inclui.
- Existe expert pessoal ou o elemento de autoridade é outro (empresa,
  método, certificação, caso)?
- Prova social disponível.
- Garantia (se houver).
- Evento de conversão desejado (formulário, checkout, agendamento).

## Dependências

- `knowledge/marketing/EXPERT_E_PAGINA_DE_OFERTA.md`
- `schemas/perfil-expert.schema.json`, `schemas/evento-conversao.schema.json`
- `templates/pagina-oferta/PAGINA_DE_OFERTA.txt`
- `.claude/skills/pagina-e-site`, `.claude/skills/design-front-end`,
  `.claude/skills/texto-natural-pt-br` (encadeamento obrigatório para a
  implementação — ver `CLAUDE.md`)

## Contexto que deve ser carregado

- `_memoria/sistema/marca.md`.
- Perfil do expert, se já registrado.

---

## Workflow

### Passo 1 — Perguntar (ver `perguntas.txt`)

Headline/promessa, público, dor, oferta, prova, demonstração, expert
(ou elemento de autoridade equivalente), CTA, FAQ, garantia, checkout,
evento de conversão.

### Passo 2 — Checar autorização de imagem

Se houver expert pessoal com foto/vídeo, confirmar autorização de uso
de imagem antes de prosseguir (`schemas/perfil-expert.schema.json`,
campo `autorizacao_de_imagem`).

### Passo 3 — Estruturar (ver `fluxo.md`)

Ordem de seções: headline/imagem do expert → prova social →
demonstração → seção sobre o expert/autoridade → oferta → FAQ → CTA.
Nem toda página usa todas as seções.

### Passo 4 — Encadear para implementação

Encaminhar para `pagina-e-site` → `design-front-end` →
`texto-natural-pt-br`, conforme `CLAUDE.md`.

### Passo 5 — Registrar evento de conversão (ver `saidas.md`)

Associar a página a um evento de conversão e, se fizer parte de
campanha, ao funil dela.

---

## Saídas

Estrutura de conteúdo da página de oferta, pronta para
`pagina-e-site`/`design-front-end`, com evento de conversão associado.

## Regras

- Nunca usar imagem/vídeo de pessoa real sem autorização confirmada.
- Nunca presumir expert pessoal quando a marca é institucional.
- Nunca confundir imagem do expert com VSL ou demonstração de produto.

## Critérios de qualidade

- Toda seção usada tem propósito claro; nenhuma seção decorativa sem
  função na conversão.

## Critérios de validação

- Evento de conversão da página registrado
  (`schemas/evento-conversao.schema.json`).

## Limitações

- Não implementa o front-end (isso é `pagina-e-site`/`design-front-end`)
  — só estrutura o conteúdo e a lógica de conversão.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]07-entregaveis/PAGINA-DE-OFERTA.md`

## Contrato de handoff

Recebe de `criar-campanha` (quando a campanha precisa de página).
Encaminha obrigatoriamente para `pagina-e-site` → `design-front-end` →
`texto-natural-pt-br`.

## Exemplos de gatilhos positivos

- "Preciso de uma página de venda pra esse produto"
- "Monta a landing page da oferta X"

## Exemplos de gatilhos negativos

- "Cria a página institucional da empresa" (sem objetivo de conversão
  direto — é `pagina-e-site` sem esta skill)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
