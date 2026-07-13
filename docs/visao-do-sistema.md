# Visão do Sistema de Apoio à Análise de LEDs

## Objetivo

O sistema apoiará arquivistas na análise de Listagens de Eliminação de Documentos (LED), comparando dados da LED com tabelas de temporalidade e destinação previamente validadas. Ele será um instrumento de apoio à decisão, não uma autoridade automática.

## Princípios obrigatórios

1. Preservar sempre os documentos originais.
2. Separar PDF original, extração, revisão humana, dados aprovados, regras automáticas, decisão humana e relatório.
3. Usar regras determinísticas, explícitas, versionadas, testáveis e auditáveis.
4. Não usar IA no núcleo decisório do MVP.
5. Não comparar LED contra tabela extraída que ainda não tenha sido revisada e aprovada.
6. Registrar proveniência, hashes, versões, transformações, decisões e auditoria.

## Fluxo de alto nível

1. Criar análise.
2. Registrar órgão, unidade, LED e analista.
3. Enviar LED em PDF.
4. Enviar ou selecionar tabela de temporalidade.
5. Extrair dados para área de revisão.
6. Revisar e aprovar dados estruturados.
7. Executar motor de regras.
8. Apresentar evidências, comentários sugeridos e resultados.
9. Registrar decisão humana.
10. Gerar relatório preliminar e final.
11. Futuramente, gerar cópia comentada do PDF, sem alterar o original.

## Situação do repositório inspecionado

O repositório atual é o projeto Operação Serenata de Amor. Ele contém dois componentes principais já existentes: Jarbas, uma aplicação Django para visualização de despesas parlamentares, e Rosie, um conjunto de classificadores em Python para identificação de suspeições em reembolsos parlamentares.

O código existente é útil como referência histórica de projeto cívico, Docker, testes e organização Python, mas não deve ser reaproveitado diretamente para o núcleo de LED porque o domínio, o modelo de dados e a arquitetura são diferentes.
