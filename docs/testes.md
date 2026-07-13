# Estratégia de Testes e Como Testar Neste Momento

## Situação atual do sistema

O sistema de apoio à análise de LEDs ainda não está implementado como aplicação executável. Nesta etapa foram criados documentos de planejamento, arquitetura, requisitos, regras de negócio, modelo de dados, extração, backlog e riscos.

Portanto, neste momento ainda não é possível testar funcionalidades como upload de PDF, extração da LED, extração da tabela de temporalidade, revisão em tela, motor de regras, geração de CSV/XLSX ou relatório final. Essas funcionalidades aparecem no backlog para as próximas etapas.

## O que pode ser testado agora

Nesta etapa, é possível testar apenas a integridade da documentação criada e confirmar que ela existe no repositório.

### Teste 1 — Verificar se os arquivos de documentação existem

**Pasta para executar:** raiz do repositório, normalmente `/workspace/serenata-de-amor`.

**Comando:**

```bash
find docs -maxdepth 1 -type f -name '*.md' | sort
```

**Para que serve:** lista os arquivos Markdown criados na pasta `docs`.

**Resultado esperado:** devem aparecer, pelo menos, estes arquivos:

- `docs/arquitetura.md`
- `docs/backlog.md`
- `docs/escopo-mvp.md`
- `docs/extracao-led.md`
- `docs/extracao-tabela-temporalidade.md`
- `docs/modelo-de-dados.md`
- `docs/regras-de-negocio.md`
- `docs/requisitos.md`
- `docs/riscos.md`
- `docs/testes.md`
- `docs/visao-do-sistema.md`

**Se ocorrer erro:**

- Se aparecer `No such file or directory`, confirme se o comando foi executado na raiz do repositório.
- Se algum arquivo não aparecer, a documentação pode não ter sido aplicada ao branch atual.

### Teste 2 — Verificar se não há problemas simples de formatação no diff

**Pasta para executar:** raiz do repositório, normalmente `/workspace/serenata-de-amor`.

**Comando:**

```bash
git diff --check HEAD~1..HEAD
```

**Para que serve:** verifica se o último commit introduziu espaços em branco problemáticos ou marcas de conflito.

**Resultado esperado:** o comando deve terminar sem mostrar mensagens.

**Se ocorrer erro:**

- Mensagens sobre `trailing whitespace` indicam espaços sobrando no fim de linhas.
- Mensagens sobre `conflict marker` indicam marcas de conflito de Git que precisam ser removidas.

### Teste 3 — Ler a documentação principal

**Pasta para executar:** raiz do repositório, normalmente `/workspace/serenata-de-amor`.

**Comando:**

```bash
sed -n '1,120p' docs/visao-do-sistema.md
```

**Para que serve:** mostra as primeiras linhas da visão do sistema para conferência manual.

**Resultado esperado:** deve aparecer a visão do sistema, seus princípios obrigatórios e a situação do repositório inspecionado.

**Se ocorrer erro:**

- Se o arquivo não existir, confirme se a documentação foi criada no branch atual.
- Se o conteúdo estiver incompleto, a etapa de documentação deve ser revisada antes de avançar.

## O que será testável na próxima etapa técnica

Quando a base técnica for criada, deverão ser testáveis:

1. Inicialização do backend.
2. Inicialização do frontend.
3. Conexão com PostgreSQL.
4. Migrações do banco.
5. Endpoint de saúde da API.
6. Upload controlado de arquivos fictícios.
7. Cálculo de hash.
8. Validação de extensão, MIME type e tamanho.
9. Testes unitários de normalização.
10. Testes unitários do motor de regras.

## O que será testável somente após os documentos de exemplo

A extração real de LED e de tabela de temporalidade só deve ser testada depois de receber cópias de trabalho, preferencialmente anonimizadas, contendo:

- LED em PDF sem comentários.
- LED já analisada.
- LED com erros conhecidos.
- LED considerada correta.
- Tabela de temporalidade em PDF.
- Tabela de temporalidade já convertida manualmente, se existir.
- Exemplos de observações, condições especiais, notas de rodapé, códigos hierárquicos e itens continuados em páginas seguintes.

Sem esses documentos, qualquer extrator seria especulativo e poderia associar campos incorretamente.

## Critério para avançar

A etapa atual pode ser considerada validada quando:

1. A equipe confirmar que a documentação reflete o processo real de análise de LEDs.
2. Os documentos de exemplo forem separados e anonimizados.
3. O escopo do MVP for aprovado.
4. As regras mínimas forem confirmadas pela equipe arquivística.
5. A arquitetura desacoplada for aceita antes da criação do backend e do frontend.
