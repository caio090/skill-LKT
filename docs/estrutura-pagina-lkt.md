# LKT | Estrutura da pagina central

## Objetivo
Uma pagina simples que permite consultar a biblioteca LKT, identificar skills por finalidade e preparar sua instalacao em projetos. Nao misturar a interface interna com REC OS nem exibir dados privados de clientes.

## Navegacao
- Inicio
- Biblioteca
- Projetos
- Instalacao
- Documentacao

## Home
1. Cabecalho: LKT System, descricao curta e acesso ao GitHub.
2. Entrada principal: "Qual projeto vamos preparar?" com acao para identificar as skills adequadas.
3. Categorias: Design e UI, Desenvolvimento, Marketing e Conteudo, Automacoes e IA, Audiovisual, Testes e Qualidade.
4. Biblioteca: busca e filtros por categoria, origem e compatibilidade.
5. Fontes: LKT locais, Kursku Skills, Superpowers, Humanizer e Dify (plataforma, nao skill). Exibir autores, licencas e status reais.
6. Como funciona: Analisar projeto > Selecionar skills > Simular instalacao > Instalar apos confirmacao > Validar.
7. Rodape: documentacao, fontes originais, licencas e historico de versoes.

## Pagina de uma skill
- Nome e descricao
- Autor e origem com link
- Categoria e compatibilidade
- Dependencias e arquivos auxiliares
- Versao ou commit fixado
- Licenca e condicoes
- Como usar
- Status: referenciada, disponivel, instalada ou validada, sem misturar os estados

## Pagina de projeto
- Nome e caminho GitHub
- Stack detectada
- Skills recomendadas e motivo
- Skills ja instaladas
- Conflitos e dependencias
- Previa do comando de instalacao
- Log de validacao

## Regras de implementacao
- Prioridade desktop e mobile sem interface poluida; acoes principais visiveis.
- Nao instalar milhares de skills indiscriminadamente.
- Nao incluir segredos nem arquivos privados na interface publica.
- Nao tratar Dify como skill do Claude Code.
- Nao declarar funcionamento de integracoes sem testes.
- A pagina e uma camada de consulta e operacao, nao uma copia das ferramentas.

## Etapas
1. Definir dados que podem ser lidos do catalogo e dos submodulos.
2. Criar wireframe e componentes.
3. Construir pagina e filtros com dados reais.
4. Conectar simulacao do instalador.
5. Adicionar instalacao real somente depois de validacao de seguranca e ambiente.
