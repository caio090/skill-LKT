# Fontes externas do LKT System

Este registro identifica os projetos upstream usados pela biblioteca LKT. LKT é o agregador e instalador; autoria, licenças e avisos originais permanecem preservados. Referenciar um projeto aqui **não** significa que seu código já foi copiado ou que está instalado.

| Fonte | URL original | Tipo | Licença | Estado na branch |
| --- | --- | --- | --- | --- |
| LKT System (Tayannara) | https://github.com/caio090/tayannara-contadora | Skills próprias e arquivos de projeto | Verificar arquivo a arquivo antes de exposição pública | Importação parcial de skills para `.claude/skills/` |
| Humanizer | https://github.com/blader/humanizer | Skill de revisão textual | MIT | SKILL.md e LICENSE importados |
| Humanizer PT-BR | https://github.com/mackswendhell/humanizer-pt-br | Skill de revisão em português brasileiro | Conferir LICENSE junto à cópia | SKILL.md e LICENSE importados |
| Superpowers | https://github.com/obra/superpowers | Coleção de skills de desenvolvimento | MIT | Inspecionado; cópia integral ainda pendente |
| Dify | https://github.com/langgenius/dify | **Plataforma completa de desenvolvimento de agentes e workflows de IA, não uma skill** | Apache 2.0 modificada, com restrições específicas | Catalogado; **não clonado** |

## Regras de integração

1. Preservar os arquivos de origem, estrutura, referências, avisos e licenças de cada fonte.
2. Não atribuir ao LKT a autoria do trabalho de terceiros. O LKT centraliza distribuição, seleção e integração.
3. Skills e plataformas não são a mesma coisa. Para skills usar `.claude/skills/<nome>/SKILL.md`; para plataformas extensas registrar um instalador/integrador próprio, mantendo o software separado para evitar um repositório gigantesco e atualizações quebradas.
4. Para Dify, conferir sua licença original antes de distribuição ou uso comercial: https://github.com/langgenius/dify/blob/main/LICENSE. O uso multi-tenant e a remoção de logo/avisos do frontend têm restrições expressas.
5. Não copiar arquivos de projetos privados, configurações secretas ou dados de clientes para a biblioteca pública.
6. O destino aprovado para o LKT é `https://github.com/caio090/skill-LKT`. Alterações devem ser revisadas na branch de migração antes de entrar na main.
