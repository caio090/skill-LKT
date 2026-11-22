# Expert e página de oferta

## Expert

Expert é a pessoa que representa o conhecimento, método, autoridade ou
produto perante o público — não é um formato de vídeo, é um papel.

**Imagem do expert** é um ativo visual (foto, vídeo curto de
apresentação), não um tipo de vídeo específico. Distinguir sempre:

- **Imagem do expert** — ativo visual de apresentação, usado no topo da
  página ou em anúncios.
- **Apresentação do expert** — seção da página contando quem é, o que
  fez, por que confiar.
- **VSL** (video sales letter) — vídeo de vendas estruturado com
  narrativa própria, diferente de uma imagem de apresentação.
- **Demonstração do produto** — mostra o produto/serviço funcionando,
  não a pessoa.
- **Depoimento** — fala de um cliente/usuário real, não do expert.
- **Prova social** — evidência agregada (número de clientes, avaliação,
  certificação, mídia), pode ou não envolver o expert diretamente.

Não presumir que toda empresa possui um expert pessoal. Em marcas
institucionais, o elemento de autoridade pode ser: fundador, equipe,
a própria empresa, o método, uma certificação, um caso de sucesso, ou
uma demonstração/prova documental — sem exigir uma pessoa central.

## Perfil do expert (quando existir)

Registrar, quando aplicável, em `_memoria.json` do workspace ou em
`schemas/perfil-expert.schema.json`: nome, papel, biografia,
experiência, credenciais, resultados, fotos, vídeos, provas,
limitações de uso do material, e autorização de imagem (sempre
confirmar que existe autorização antes de usar imagem/vídeo de uma
pessoa real em material público).

## Página de oferta

Estrutura de referência (nem toda página usa todas as seções — a skill
`estruturar-pagina-de-oferta` decide conforme o caso):

1. Headline e imagem do expert (ou elemento de autoridade equivalente)
2. Prova social
3. Demonstração (do produto, método ou resultado)
4. Seção sobre o expert (ou sobre a empresa/método, quando não houver
   expert pessoal)
5. Oferta (o que é, o que inclui, condições)
6. FAQ
7. CTA (chamada para ação — ligada a um evento de conversão registrado)

Toda página de oferta se conecta a um evento de conversão (ver
`schemas/evento-conversao.schema.json`) e, quando fizer parte de uma
campanha, ao funil associado (`schemas/funil.schema.json`,
`campanha_id`).

Ver `.claude/skills/estruturar-pagina-de-oferta/SKILL.md` e
`templates/pagina-oferta/PAGINA_DE_OFERTA.txt`.
