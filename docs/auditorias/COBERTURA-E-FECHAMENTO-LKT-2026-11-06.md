# LKT System | Auditoria consolidada de cobertura e fechamento

Data-base: 2026-11-06
Status: documento de trabalho na branch `feat/importar-skills-lkt-completas`. Não implica merge, deploy ou instalação local.

## 1. Fontes e números que não devem ser confundidos

**Inventário local recebido do Claude (recorte do computador):**
- 1.126 arquivos `SKILL.md` encontrados; 834 nomes distintos no computador.
- 244 skills distintas consideradas instaladas ou potencialmente utilizáveis.
- 103 skills no LKT examinado naquele inventário; 141 fora.
- 134 nomes com cópias múltiplas (119 idênticas, 15 divergentes).
- Classificação das 141: 6 candidatas, 30 para verificar, 105 não incorporar.

**Estado confirmado do GitHub na branch atual (checagem de árvore):**
- 163 arquivos `.claude/skills/<nome>/SKILL.md`, sem duplicação de caminho.
- O catálogo declara 127 skills do núcleo LKT, 2 do LKT Plus e 34 de terceiros.
- Portanto, **103 e 163 não são o mesmo recorte nem devem ser somados**. Fazer comparação por hash, nome, origem, versão e caminho para determinar quais 103 estão entre as 163.
- O CSV local do relatório, em `/private/tmp/claude-501/.../scratchpad/inventario-skills-lkt.csv`, não está versionado; não alegar que foi incorporado antes de recebê-lo e conferir dados e licenças.

## 2. Estado real das 6 candidatas do relatório

| Skill | GitHub `.claude/skills` | Decisão |
|---|---|---|
| apple-design | ausente | avaliar importação MIT preservando fonte, versão e LICENSE |
| canvas-design | presente | auditar versão, integridade e licença; não duplicar |
| theme-factory | presente | auditar versão, integridade e licença; não duplicar |
| web-artifacts-builder | presente | auditar dependências e licença; não duplicar |
| supabase-postgres-best-practices | ausente | avaliar importação MIT e testes da aplicação |
| n8n-workflow-check | ausente | avaliar importação MIT e conexão ao fluxo n8n |

**Observação:** estar presente não significa que a ferramenta executou com sucesso no Claude, Codex ou ChatGPT. Fazer testes por ambiente.

## 3. Pendências que bloqueiam declaração de cobertura completa

1. **Identidade do sistema:** README apresenta "REC OS", enquanto repositório e objetivo são "LKT System". Definir nomenclatura canônica e histórico de migração, preservando links antigos.
2. **Inventário verificável:** gerar catálogo a partir de arquivos reais com campos `id, nome, origem, licença, versão, hash, categoria, ambiente, dependências, status, testes, fonte`.
3. **Instalador:** `tools/instalar_lkt.py` instala apenas em `.claude/skills` e oferece perfis base/web/marketing/automacao. Adicionar destino Codex, seleção explícita, dry-run padrão, conflitos, rollback, sincronização de versão e relatório de instalação, sem sobrescrever por padrão.
4. **E-commerce:** criar skill autoral `ecommerce-loja` que cubra catálogo, variantes, estoque, checkout, frete, pagamento, SEO, políticas e integrações. NÃO importar Shopify automaticamente.
5. **Teste ponta a ponta:** criar skill autoral `qa-e2e-playwright`, com fluxos reais, dados sintéticos, smoke test, screenshots, testes mobile, acessibilidade e proibição de alterar produção.
6. **Remotion:** revisar as 12 versões, atualizar da origem, conservar licença das skills e verificar separadamente a licença comercial do framework. O plugin e o framework são coisas distintas.
7. **React/Vercel:** validar proveniência e licença da skill `react-best-practices` antes de qualquer cópia.
8. **Plugins design/marketing Anthropic:** preferir referência/instalação de origem quando a licença específica não estiver clara; mapear equivalências e colisões com o LKT.
9. **Duplicatas:** não fundir por nome isolado; comparar hashes, manifesto, versão, autor e comportamento. Resolver `pdf`, `skill-creator` e `edit-premiere-project` por namespace.
10. **Qualidade:** catálogo automatizado, validação de frontmatter e links, testes de instalação em projeto isolado, matriz Claude Code/Codex/ChatGPT, testes de carga seletiva e registro de regressões.
11. **Segurança:** repositório é público. Antes de publicar, varrer credenciais, tokens, arquivos privados, dados de clientes, tabelas de preços, históricos e materiais com restrição de redistribuição.
12. **Projeto Tayannara, Dify e instalador:** concluir auditoria e compatibilidade desses componentes antes de habilitar combo automático para todos os projetos.

## 4. Arquitetura de destino

- `.claude/skills/`: skills efetivamente aprovadas para Claude, com um único ID canônico.
- `terceiros/`: integrações e bibliotecas relacionadas a ambientes específicos, sem cópias proprietárias.
- `docs/catalogo-skills.md`: catálogo humano gerado de manifesto versionado.
- `docs/auditorias/`: evidências, inventários e aceite de cada rodada.
- `docs/compatibilidade.md`: matriz de execução por plataforma.
- `docs/roteamento.md`: regras de seleção por intenção, precedência, conflito e fallback.
- `tools/`: descoberta, sincronização, instalador, verificação, testes e rollback.
- `vendor/`: apenas referências/submódulos permitidos, com fonte e licença.

**Princípio:** biblioteca central única, execução seletiva por projeto. Não instalar centenas de skills em cada projeto.

## 5. Ordem de implementação e aceite

### Fase A: saneamento
- [ ] Unificar nomenclatura LKT / REC OS no README e docs.
- [ ] Versionar inventário validado e cruzar 103 vs 163 vs 244 sem somar recortes.
- [ ] Auditar atribuição e licença dos 34 terceiros e bibliotecas de submódulos.
- [ ] Resolver documentação de `qa` e registrar skills aposentadas.
- [ ] Validar segurança de repositório público.

### Fase B: cobertura
- [ ] Auditar as 3 candidatas já presentes.
- [ ] Avaliar e adicionar as 3 candidatas ausentes.
- [ ] Criar `ecommerce-loja` e `qa-e2e-playwright` com testes.
- [ ] Resolver Remotion, React/Vercel e plugins dependentes de plataforma.

### Fase C: distribuição
- [ ] Instalação seletiva para Claude Code e Codex.
- [ ] Documentar explicitamente o que ChatGPT pode ler e executar; não prometer instalação automática de skills locais no ChatGPT.
- [ ] Perfis por projeto, simulação, relatórios, controle de colisão e rollback.
- [ ] Revisar Tayannara, Dify e integrador antes de ativação global.

### Fase D: auditoria final
- [ ] Comparar manifesto e árvore de arquivos automaticamente.
- [ ] Executar validador e testes em projetos descartáveis.
- [ ] Confirmar que nenhuma skill foi copiada sem licença redistribuível.
- [ ] Conferir que `main` e produção ficaram intactas até revisão de PR.
- [ ] Emitir relatório com `aprovado`, `pendente`, `referência externa`, `bloqueado`.

## 6. Políticas operacionais

- Preservar autoria, LICENSE original, URLs de origem e commit de referência.
- Nunca reescrever uma skill de terceiros como autoria LKT.
- Nunca executar comandos destrutivos ou fazer merge/deploy automaticamente.
- Nunca conectar projetos ao Supabase de produção apenas para testar skills.
- Sempre utilizar o padrão visual e textual LKT quando aplicável, sem inserir a sigla em peças dos clientes.
- Documento de auditoria não é prova de implementação: fechar cada checkbox com evidência.

## 7. Nota de reconciliação

O PR #1 declara 163 skills e já inclui `canvas-design`, `theme-factory` e `web-artifacts-builder`, enquanto o relatório local classificou essas três como futuras candidatas. A verificação da árvore explica a discrepância sem apagar o inventário original. O passo seguinte é comparar arquivo por arquivo, não importar novamente.

---

## 8. Fechamento da rodada de 2026-11-06 (execução no Claude Code)

Branch `feat/importar-skills-lkt-completas`, commits `ec6cbcd`..`HEAD`.
`main` e produção **não** foram alteradas. Nenhum merge, deploy ou force push.

### Concluído (com evidência)

| Item | Evidência |
|---|---|
| Inventário reconciliado 103 × 163 × 244 por hash | `docs/auditorias/RECONCILIACAO-2026-11-06.{md,csv}` |
| Registro canônico + schema + verificação | `registry/`, `tools/registro.py check` → OK |
| Catálogo gerado do registro (inclui `qa`) | `docs/catalogo-skills.md`; CI confere com `--catalogo` |
| 6 candidatas | 3 já presentes conferidas como idênticas ao upstream (`canvas-design`, `theme-factory`, `web-artifacts-builder`); 3 importadas com LICENSE e commit de origem (`ec6cbcd`) |
| Licença dos 34 terceiros em `.claude/skills` | Todas com arquivo de licença; licença do upstream conferida via API GitHub; 12 idênticas, 18 versão anterior, 4 sem caminho verificável (`registry/fontes.json`) |
| `ecommerce-loja` com exemplos e testes | `tests/link-whatsapp.test.js` 5/5 |
| `qa-e2e-playwright` com exemplos e testes | Suíte de exemplo 8/8 (Playwright 1.56.1, desktop + mobile, rede bloqueada) |
| Instalador: dry-run padrão, seletivo, idempotente, conflito, update, rollback, desinstalação, traversal/symlink | `tests/test_instalador.py` 18/18; Cenário J executado em projeto vazio |
| React/Vercel: proveniência | `vercel/vercel-plugin`, Apache-2.0; cópia = versão anterior; não promovida |
| Remotion: decisão de licença separada do framework | `docs/licencas.md`; estado `bloqueada` |
| Políticas de sandbox Supabase/n8n | `docs/sandbox.md` |
| Validador: avisos classificados | 56 problemas → 0; 15 avisos, todos de conteúdo de terceiros |
| README/identidade LKT System, histórico preservado | `README.md`, `docs/MIGRACAO.md` |
| Segredos | Varredura de padrões (chaves OpenAI/GitHub/AWS/Google/Slack, JWT, chave privada) na árvore e no histórico: 0 ocorrências. `_memoria/` só tem modelos vazios |
| CI segura (modelo) | `docs/ci/validar.yml` (sem deploy, sem segredos); ativação pendente, ver abaixo |

### Parcial

- Compatibilidade Codex: formato válido; nenhuma skill executada no Codex nesta rodada.
- Cenários A, B, D, E, F, G, H, I: definidos em `docs/roteamento.md`, não executados.
- Windows: não testado.
- 18 skills de terceiros em versão anterior ao upstream: registradas, não atualizadas.

### Pendente (decisão humana)

- **LICENSE da raiz** para o conteúdo autoral (ou tornar o repositório privado).
- Plugins Codex `supabase`, `google-drive`, `documents`, `pdf`, `presentations`, `spreadsheets`: texto de licença oficial não localizado.
- `CLAUDE.md`/`AGENTS.md` ainda citam `modules/` e `templates/` inexistentes.
- Descrição do PR #1: não atualizada automaticamente (sem `gh` CLI nem token de API nesta máquina). Texto sugerido no relatório da sessão.
- Submódulo `vendor/kursku-skills` não tem licença: permanece só como referência.

### Bloqueado

- `terceiros/codex/plugins/remotion` (12 skills): conflito entre a LICENSE MIT da cópia e a Remotion License do upstream. Continua no repositório, marcado como `bloqueada`; **remover ou manter é decisão do dono** (o conteúdo já está público no histórico da branch).

### Não aplicável

- Importar Shopify ou plugins proprietários: fora da política.

### Nota sobre a CI

O push com `.github/workflows/validar.yml` foi recusado pelo GitHub: o token
desta máquina não tem o escopo `workflow`. O arquivo foi movido para
`docs/ci/validar.yml` antes de qualquer envio (o workflow nunca chegou ao
remoto). Ativação: copiar para `.github/workflows/` pela interface do GitHub.
