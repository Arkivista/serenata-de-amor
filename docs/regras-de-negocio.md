# Regras de Negócio

## Estados de resultado

- CONFORME
- DIVERGENTE
- INFORMAÇÃO AUSENTE
- CORRESPONDÊNCIA PARCIAL
- CÓDIGO NÃO LOCALIZADO
- TABELA INAPLICÁVEL
- NECESSITA ANÁLISE HUMANA
- NÃO VERIFICADO
- ERRO DE EXTRAÇÃO
- REGRA NÃO APLICÁVEL
- INSTRUMENTO NÃO VIGENTE

## Regras mínimas do MVP

- LED-COD-001: verificar se o código informado na LED existe na tabela selecionada.
- LED-COD-002: comparar códigos após normalizações autorizadas, preservando o original.
- LED-COD-003: verificar aplicabilidade do código ao órgão, atividade ou período.
- LED-DES-001: verificar correspondência exata ou normalizada do descritor.
- LED-DES-002: sinalizar correspondência parcial sem equivalência semântica automática.
- LED-TEMP-001: comparar prazo da fase corrente.
- LED-TEMP-002: comparar ou sinalizar evento de contagem da fase corrente.
- LED-TEMP-003: comparar prazo da fase intermediária.
- LED-TEMP-004: comparar ou sinalizar evento de contagem da fase intermediária.
- LED-DEST-001: comparar destinação final; guarda permanente nunca deve ser tratada como eliminação automática.
- LED-DATA-001: verificar cumprimento de prazo somente quando houver dados suficientes.
- LED-OBS-001: sinalizar observação, ressalva ou condição especial para análise humana.
- LED-CONS-001: verificar consistência entre código, descritor, prazos e destinação.
- LED-CAMP-001: identificar campos obrigatórios ausentes.
- LED-INST-001: verificar vigência do instrumento.
- LED-INST-002: verificar inadequação do instrumento ao órgão, atividade ou universo documental.

## Catálogo inicial de comentários

Comentários devem ser técnicos, impessoais, editáveis e preferencialmente iniciar por verbo no infinitivo. Exemplos: corrigir código, adequar descritor, corrigir prazo, corrigir destinação, verificar cumprimento de prazo, complementar informações, esclarecer condição especial e verificar aplicabilidade da tabela.
