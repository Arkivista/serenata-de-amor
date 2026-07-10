# Extração da Tabela de Temporalidade

## Premissas

A tabela de temporalidade não deve ser tratada como planilha simples. Códigos podem ser hierárquicos; descritores podem quebrar linha; células vazias podem representar repetição visual; notas e condições podem alterar prazo ou destinação.

## Ordem de processamento

1. Usar camada de texto.
2. Analisar coordenadas, linhas e colunas.
3. Avaliar bibliotecas como PyMuPDF e pdfplumber após ver os PDFs.
4. Aplicar regras específicas do modelo identificado.
5. Usar OCR somente se necessário.
6. Registrar método e confiança por página.
7. Encaminhar ambiguidades para validação humana.

## Estrutura mínima de CSV

- codigo
- codigo_pai
- nivel_hierarquico
- descritor
- prazo_corrente
- evento_contagem_corrente
- prazo_intermediario
- evento_contagem_intermediaria
- destinacao_final
- observacao
- condicao_especial
- referencia_normativa
- pagina_origem
- linha_origem
- confianca_extracao
- status_validacao

## Falhas de extração

Quando não houver segurança, o sistema deve indicar páginas e campos afetados, permitir correção manual, impedir aprovação automática e registrar a ocorrência.

## Bibliotecas a avaliar

- PyMuPDF: bom para texto, coordenadas e recortes visuais.
- pdfplumber: bom para tabelas com linhas e coordenadas.
- Camelot e Tabula: úteis em alguns PDFs tabulares, mas dependem do padrão do arquivo.
- OCRmyPDF e Tesseract: usar somente em PDF digitalizado.
- OpenCV: útil para detecção visual avançada, se necessário.
- pandas e openpyxl: úteis para CSV/XLSX, não para decidir regras arquivísticas.
