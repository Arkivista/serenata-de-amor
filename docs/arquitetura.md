# Arquitetura Recomendada

## Decisão arquitetural inicial

Recomenda-se criar um novo produto desacoplado dentro do repositório, em diretórios `backend/`, `frontend/`, `samples/` e `scripts/`, sem alterar Jarbas e Rosie. O repositório atual é Django legado com Elm e classificadores Python; reaproveitá-lo diretamente aumentaria o risco de acoplamento indevido.

## Backend

- Python.
- FastAPI para API HTTP.
- SQLAlchemy para acesso ao banco.
- Pydantic para validação de dados.
- Alembic para migrações.
- PostgreSQL para dados estruturados.
- PyMuPDF e pdfplumber, após análise dos PDFs, para extração com camada de texto.
- pandas e openpyxl para CSV/XLSX.
- pytest para testes.

## Frontend

Recomenda-se React com TypeScript e Vite no MVP. A escolha reduz complexidade em comparação com Next.js, pois o sistema inicial não precisa de renderização no servidor. O frontend deve usar componentes acessíveis, textos em português do Brasil, filtros, tabelas revisáveis e visualização lado a lado de evidências.

## Camadas lógicas

1. API e autenticação.
2. Serviço de armazenamento de arquivos.
3. Extração de LED.
4. Extração de tabela de temporalidade.
5. Normalização.
6. Revisão e aprovação humana.
7. Motor de regras determinístico.
8. Comentários padronizados.
9. Relatórios.
10. Auditoria.
11. Adaptadores opcionais de IA, desacoplados e inativos por padrão.

## Integração futura com IA

A interface de IA deve receber entrada explícita, registrar fornecedor, modelo, finalidade, dados enviados, confiança e retorno. Ela nunca deve alterar resultado definitivo, aprovar tabela, aprovar LED ou modificar códigos, prazos e destinações sem validação humana.

## Comandos úteis de inspeção já utilizados

- `pwd`: confirma a pasta atual.
- `find .. -name AGENTS.md -print`: procura instruções locais para agentes.
- `rg --files`: lista arquivos do repositório sem varredura recursiva lenta.
- `git status --short`: verifica alterações locais.
- `sed -n`: lê trechos de arquivos de configuração e documentação.
