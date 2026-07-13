# Modelo de Dados Inicial

## Entidades principais

- Usuário: pessoa que acessa o sistema.
- Perfil: conjunto de responsabilidades, como analista, revisor, administrador ou auditor.
- Permissão: ação autorizada no sistema.
- Órgão: órgão ou entidade relacionada à LED.
- Unidade: unidade produtora ou acumuladora.
- Arquivo armazenado: arquivo preservado com nome seguro, hash, MIME type, tamanho e localização.
- Documento: abstração para LED, tabela, relatório e exportações.
- LED: listagem submetida para análise.
- Linha da LED: item documental da LED.
- Campo extraído: valor com proveniência, coordenadas, método, confiança e necessidade de revisão.
- Instrumento de temporalidade: tabela ou instrumento normativo.
- Versão do instrumento: versão aprovada, vigente, substituída ou revogada.
- Item da tabela: linha estruturada da tabela de temporalidade.
- Nota da tabela: nota de rodapé, observação geral ou ressalva vinculável a itens.
- Análise: processo que une LED, tabela, usuário e execução de regras.
- Execução de regra: registro da aplicação de uma versão de regra.
- Resultado: conclusão automática com evidência e comentário sugerido.
- Comentário padronizado: mensagem versionada associada a regra e campo.
- Comentário editado: texto final ajustado pelo arquivista.
- Decisão humana: aceite, rejeição, dúvida, edição ou aprovação.
- Relatório: documento gerado com síntese, detalhamento e hashes.
- Evento de auditoria: trilha de ações e alterações.
- Extrator e versão do extrator: componente que produziu dados extraídos.
- Regra e versão da regra: componente determinístico aplicado.
- Integração de IA e operação de IA: registros futuros, opcionais e não decisórios.

## Relacionamentos e cardinalidades

- Um órgão possui muitas unidades.
- Uma análise pertence a uma LED e a uma versão de instrumento.
- Uma LED possui muitas linhas.
- Uma linha possui muitos campos extraídos.
- Um instrumento possui muitas versões.
- Uma versão de instrumento possui muitos itens da tabela e notas.
- Uma análise possui muitas execuções de regra.
- Uma execução de regra produz muitos resultados.
- Um resultado pode ter uma decisão humana e um comentário editado.
- Um arquivo armazenado pode estar associado a documentos originais, CSV, XLSX, relatórios e PDFs futuros comentados.

## Dados sensíveis e proteção

Podem existir nomes, assinaturas, cargos, unidades internas e metadados administrativos. Logs não devem expor conteúdo documental completo. Arquivos devem ser armazenados com nomes seguros e acesso controlado.

## Versionamento, exclusão e retenção

Versões aprovadas de instrumentos não devem ser sobrescritas. Correções relevantes devem gerar histórico ou nova versão. Exclusões devem ser controladas, auditadas e preferencialmente lógicas quando houver necessidade de rastreabilidade institucional.
