# Escopo do MVP

## Incluído no MVP

- Criar análise de LED.
- Receber LED em PDF de formulário inicialmente padronizado.
- Receber tabela de temporalidade em PDF com camada de texto, CSV ou XLSX.
- Calcular hash dos documentos recebidos.
- Preservar arquivos originais.
- Extrair dados para uma camada de dados não validados.
- Permitir revisão e correção humana.
- Aprovar tabela estruturada antes de uso em regras.
- Gerar CSV e XLSX da tabela validada.
- Executar regras determinísticas mínimas.
- Apresentar evidências, página, linha e campo quando disponíveis.
- Sugerir comentários padronizados editáveis.
- Registrar aceite, rejeição, edição e justificativa do arquivista.
- Gerar relatório de conformidade em HTML e, depois, PDF.
- Registrar auditoria e versionamento.

## Fora do MVP

- Extrator universal para qualquer PDF.
- Uso obrigatório de OCR.
- Uso de API paga.
- Envio de documentos a serviços externos.
- Decisão automática final sobre conformidade da LED.
- Anotação visual do PDF original.
- IA no núcleo de regras.

## Critérios de aceite do MVP

1. A análise pode ser criada e identificada.
2. A LED e a tabela podem ser importadas sem alterar os originais.
3. A tabela extraída só pode ser usada após aprovação humana.
4. As regras mínimas retornam estados padronizados.
5. Cada divergência possui evidência e comentário sugerido.
6. O arquivista pode aceitar, rejeitar ou editar apontamentos.
7. O relatório final contém síntese, detalhamento e hashes.
8. Os testes automatizados passam.
9. O sistema roda localmente com Docker Compose.
10. Nenhuma API de IA é necessária.

## Documentos de exemplo necessários

- LED sem comentários.
- LED já analisada.
- LED com erros conhecidos.
- LED considerada correta.
- Tabela de temporalidade em PDF com camada de texto.
- Tabela equivalente convertida manualmente, se existir.
- Catálogo de comentários usados pela equipe.
- Relatório ou manifestação real, preferencialmente anonimizado.
- Lista de campos obrigatórios do formulário.
- Regras internas atualmente adotadas.
- Exemplos de condições especiais, códigos hierárquicos, notas e itens continuados.
