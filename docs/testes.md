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

## Testes após a criação da base técnica inicial

A base técnica inicial adiciona um backend FastAPI mínimo. Ela ainda não analisa PDFs, mas já permite testar se a API pode ser importada e se as regras de configuração mantêm IA desligada por padrão.

### Teste 4 — Executar testes unitários do backend

**Pasta para executar:** `backend`.

**Comando:**

```bash
PYTHONPATH=. pytest
```

**Para que serve:** executa os testes automatizados básicos do backend.

**Resultado esperado:** os testes de configuração e contrato de IA devem passar.

**Se ocorrer erro:**

- Se aparecer `ModuleNotFoundError: No module named 'fastapi'`, instale as dependências em um ambiente virtual com `pip install -r requirements/dev.txt` dentro da pasta `backend`.
- Se aparecer erro de importação de `app`, confirme se o comando foi executado dentro da pasta `backend` e se `PYTHONPATH=.` foi informado.

### Teste 5 — Subir a API manualmente

**Pasta para executar:** `backend`.

**Comando:**

```bash
uvicorn app.main:app --reload
```

**Para que serve:** inicia a API de desenvolvimento.

**Resultado esperado:** a API deve iniciar e o endereço `http://127.0.0.1:8000/health` deve retornar `status: ok`.

**Se ocorrer erro:**

- Se `uvicorn` não existir, instale as dependências com `pip install -r requirements/dev.txt`.
- Se a porta 8000 estiver em uso, encerre o processo anterior ou use outra porta, por exemplo `uvicorn app.main:app --reload --port 8001`.

### Teste 6 — Testar validação e armazenamento local sem API HTTP

**Pasta para executar:** `backend`.

**Comando:**

```bash
PYTHONPATH=. pytest tests/test_file_validation.py tests/test_local_storage.py
```

**Para que serve:** verifica se o sistema aceita somente extensões previstas, rejeita arquivos vazios, rejeita MIME type incompatível e preserva o conteúdo original em armazenamento local de teste.

**Resultado esperado:** todos os testes devem passar.

**Se ocorrer erro:**

- Se aparecer erro de importação, confirme que o comando foi executado dentro de `backend`.
- Se aparecer falha de validação, revise a extensão, o MIME type e o tamanho do arquivo usado no teste.

### Teste 7 — Testar upload manual pela API

**Pasta para executar:** `backend`.

**Pré-condição:** a API precisa estar iniciada com `uvicorn app.main:app --reload`.

**Comando:**

```bash
curl -F "document_kind=led" -F "file=@/caminho/para/led-ficticia.pdf;type=application/pdf" http://127.0.0.1:8000/documents
```

**Para que serve:** envia uma LED fictícia em PDF para o protótipo, calcula hash e preserva o arquivo original.

**Resultado esperado:** resposta JSON com identificador, hash SHA-256, tamanho, nome original, nome seguro e status `recebido_preservado_original`.

**Se ocorrer erro:**

- `400 Bad Request`: confira se `document_kind` é `led` e se o arquivo é PDF.
- `curl: Failed to connect`: confirme se a API está rodando.
- `ModuleNotFoundError`: instale as dependências com `pip install -r requirements/dev.txt`.

### Teste 8 — Testar normalização e primeiras regras determinísticas

**Pasta para executar:** `backend`.

**Comando:**

```bash
PYTHONPATH=. pytest tests/test_normalization.py tests/test_rules_engine.py
```

**Para que serve:** valida a normalização controlada de textos e códigos, além das primeiras regras determinísticas do MVP com dados fictícios.

**Resultado esperado:** os testes devem indicar que código correto fica conforme, descritor divergente é apontado, prazos corretos ficam conformes, destinação divergente é apontada e observação da tabela exige análise humana.

**Se ocorrer erro:**

- Se o erro indicar divergência de resultado esperado, revise a regra correspondente antes de integrar com qualquer PDF.
- Se o erro indicar importação, confirme que o comando foi executado dentro de `backend` com `PYTHONPATH=.`.

### Teste 9 — Testar o endpoint de protótipo do motor de regras

**Pasta para executar:** `backend`.

**Pré-condição:** a API precisa estar iniciada com `uvicorn app.main:app --reload`.

**Comando:**

```bash
curl -X POST http://127.0.0.1:8000/rules/evaluate-line \
  -H "Content-Type: application/json" \
  -d '{"led_line":{"line_id":"linha-1","codigo":"023.15","descritor":"Folhas de frequência","prazo_corrente":"5 anos","prazo_intermediario":"não se aplica","destinacao_final":"guarda permanente"},"approved_items":[{"codigo":"023.15","descritor":"Controle de frequência","prazo_corrente":"5 anos","prazo_intermediario":"não se aplica","destinacao_final":"eliminação","status_validacao":"aprovado"}]}'
```

**Para que serve:** permite testar o motor de regras sem depender ainda da extração de PDF.

**Resultado esperado:** a resposta deve indicar `CONFORME` para código e prazos, `DIVERGENTE` para descritor e destinação final.

**Se ocorrer erro:**

- `curl: Failed to connect`: confirme se a API está rodando.
- `422 Unprocessable Entity`: confira se o JSON contém `led_line` e `approved_items`.
- Resultado inesperado: revise a regra antes de integrar com dados extraídos de PDF.

### Teste 10 — Testar análise estruturada em lote e relatório HTML

**Pasta para executar:** `backend`.

**Comando:**

```bash
PYTHONPATH=. pytest tests/test_structured_analysis.py
```

**Para que serve:** valida um protótipo funcional sem PDF, comparando múltiplas linhas estruturadas com uma tabela aprovada fictícia e gerando HTML preliminar.

**Resultado esperado:** o teste deve confirmar a síntese de resultados e a presença dos detalhes no relatório HTML.

**Se ocorrer erro:**

- Se a contagem de resultados estiver errada, revise as regras antes de usar documentos reais.
- Se o HTML não contiver os dados esperados, revise o gerador de relatório antes de evoluir para PDF ou DOCX.

### Teste 11 — Testar sem instalar nada, abrindo um arquivo HTML local

**Pasta para executar:** raiz do repositório.

**Arquivo:** `samples/prototipo-led-navegador.html`.

**Como testar:** abra esse arquivo diretamente no navegador, sem Docker e sem instalar Python.

**Para que serve:** permite validar comigo, antes de subir o contêiner localmente, o comportamento esperado do motor de regras com dados fictícios estruturados.

**Resultado esperado:** ao clicar em `Executar análise no navegador`, a página deve mostrar uma síntese com resultados `CONFORME` e `DIVERGENTE`, além de uma tabela detalhada com comentários sugeridos.

**Limitação:** esse teste local replica a lógica principal em JavaScript para demonstração. O teste oficial do backend continua sendo feito pelo Python/FastAPI e pelos testes automatizados.
