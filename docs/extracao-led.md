# Extração da LED

## Premissas

O MVP aceitará inicialmente PDFs de LED em um formulário padronizado. O extrator será específico para esse padrão e implementado somente após análise de documentos fictícios, anonimizados ou cópias de trabalho.

## Dados mínimos pretendidos

Órgão, unidade produtora, unidade acumuladora, número e ano da LED, página, linha, código, descritor, assunto ou série, datas-limite, prazos, evento de contagem, destinação, quantidade, unidade de arquivamento, mensuração, observações, instrumento informado, assinaturas, aprovações e campos obrigatórios.

## Metadados por campo

Cada campo deve registrar valor original, valor normalizado, documento, página, linha, campo, coordenadas aproximadas, método de extração, confiança, transformação aplicada, necessidade de revisão, data e versão do extrator.

## Estratégia

1. Preservar o PDF original.
2. Calcular hash.
3. Verificar camada de texto.
4. Identificar modelo do formulário.
5. Localizar cabeçalhos, colunas, linhas e células.
6. Extrair dados para área não validada.
7. Marcar falhas e ambiguidades.
8. Exigir revisão humana antes de uso no motor de regras.

## Restrições

Não usar OCR se houver camada de texto utilizável. Não inferir valores ausentes. Não modificar o PDF original.
