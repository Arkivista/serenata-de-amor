# Requisitos

## Atores

- Arquivista analista: conduz a análise, revisa extrações e decide apontamentos.
- Revisor ou coordenador: aprova tabelas, relatórios e decisões sensíveis.
- Administrador do sistema: gerencia usuários, perfis, configurações e retenção.
- Auditor: consulta trilhas de auditoria e relatórios.

## Requisitos funcionais

- RF-001: criar análise com identificação de órgão, unidade, LED, ano e analista.
- RF-002: fazer upload de LED em PDF.
- RF-003: fazer upload de tabela em PDF, CSV ou XLSX.
- RF-004: selecionar tabela previamente aprovada.
- RF-005: calcular hash criptográfico de arquivos.
- RF-006: extrair dados de LED padronizada.
- RF-007: extrair dados de tabela PDF com camada de texto.
- RF-008: registrar valor original, normalizado, página, linha, campo, coordenadas, método, confiança e versão do extrator.
- RF-009: permitir revisão e correção dos dados extraídos.
- RF-010: aprovar tabela estruturada por usuário autorizado.
- RF-011: impedir uso de tabela não aprovada no motor de regras.
- RF-012: gerar CSV e XLSX vinculados ao PDF original.
- RF-013: executar regras mínimas de código, descritor, temporalidade, destinação, datas, observações, consistência, campos obrigatórios e instrumento.
- RF-014: apresentar evidência de cada verificação.
- RF-015: sugerir comentários padronizados.
- RF-016: permitir aceite, rejeição, edição e observação manual.
- RF-017: gerar relatório HTML e PDF.
- RF-018: registrar auditoria de eventos relevantes.

## Requisitos não funcionais

- RNF-001: funcionar localmente sem serviços pagos.
- RNF-002: não depender de IA no MVP.
- RNF-003: proteger credenciais por variáveis de ambiente.
- RNF-004: validar extensão, MIME type e tamanho de arquivos.
- RNF-005: produzir logs estruturados sem expor dados pessoais desnecessários.
- RNF-006: seguir boas práticas de acessibilidade, incluindo uso por teclado, foco visível e textos em português do Brasil.
- RNF-007: manter regras, extratores e normalizadores testáveis isoladamente.
