# Backend do Sistema de Apoio à Análise de LEDs

Este backend é a base técnica inicial do MVP. Ele ainda não implementa extração, motor de regras ou relatórios, mas já permite testar saúde da API e importação controlada de arquivos originais.

## O que existe agora

- Aplicação FastAPI mínima.
- Endpoint `/health` para verificar se a API iniciou.
- Endpoint `POST /documents` para receber LED em PDF ou tabela de temporalidade em PDF/CSV/XLSX.
- Validação determinística de tipo documental, extensão, MIME type e tamanho.
- Cálculo de hash SHA-256 do arquivo original.
- Preservação do arquivo original com nome seguro em armazenamento local.
- Registro de metadados em JSON ao lado do arquivo preservado.
- Configuração por variáveis de ambiente.
- IA desativada por padrão.
- Interface desacoplada para futuras sugestões de IA, sem poder decisório.
- Testes unitários básicos de configuração, contrato de IA, validação de arquivos e armazenamento local.

## Como executar futuramente

Na pasta `backend`, após instalar as dependências em ambiente virtual:

```bash
uvicorn app.main:app --reload
```

Resultado esperado: a API deve iniciar e expor `/health`.

## Como testar

Na pasta `backend`, com as dependências de desenvolvimento instaladas:

```bash
PYTHONPATH=. pytest
```

Resultado esperado: todos os testes passam.

## Exemplo de upload manual

Na pasta `backend`, com a API iniciada e usando um PDF fictício:

```bash
curl -F "document_kind=led" -F "file=@/caminho/para/led-ficticia.pdf;type=application/pdf" http://127.0.0.1:8000/documents
```

Resultado esperado: resposta JSON com `document_id`, `sha256`, tamanho, nome original, nome seguro e status `recebido_preservado_original`.
