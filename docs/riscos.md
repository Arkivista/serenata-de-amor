# Riscos

## Riscos técnicos

- O repositório atual é legado e usa Django 2.1, Elm 0.18 e dependências antigas; misturar o novo sistema com esse código pode aumentar manutenção e riscos de segurança.
- PDFs podem ter ordem interna de texto diferente da ordem visual.
- Tabelas podem conter células mescladas, notas, itens continuados e hierarquias difíceis de extrair automaticamente.
- OCR pode produzir dados imprecisos e deve exigir validação humana.
- Dependências como Camelot, Tabula, Tesseract e OpenCV podem exigir pacotes nativos e aumentar complexidade do ambiente.

## Riscos arquivísticos

- Associar código, descritor, prazo e destinação incorretamente pode gerar apontamento indevido.
- Ignorar observações, ressalvas e notas pode alterar o sentido da tabela.
- Considerar correspondência semântica automática no MVP pode ocultar divergências.
- Usar tabela não vigente ou inaplicável pode invalidar a análise.

## Mitigações

- Implementar extratores específicos por modelo, não universais.
- Preservar originais e registrar hashes.
- Exigir aprovação humana antes do motor de regras.
- Registrar confiança e falhas.
- Criar testes com dados fictícios.
- Separar extração, normalização, regras e decisão humana.
- Manter IA opcional, auditável e fora do núcleo decisório.

## Próximo passo recomendado

Receber documentos de exemplo anonimizados para análise visual e estrutural antes de implementar extratores.
