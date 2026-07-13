# Execução e Instalação do Protótipo

## Resposta direta

A opção recomendada para o MVP é executar o sistema em **contêineres Docker**, usando Docker Compose. Essa abordagem evita instalar Python, PostgreSQL e dependências diretamente na máquina do usuário final e facilita a implantação em infraestrutura interna.

O sistema também poderá ser executado por instalação local para desenvolvimento técnico, mas essa não deve ser a forma preferencial para arquivistas.

Nesta fase, o sistema **não é um arquivo executável único** como `.exe`, `.app` ou instalador gráfico. Essa possibilidade pode ser estudada futuramente, mas não é a recomendação inicial para um sistema web com banco de dados, upload de documentos, auditoria e múltiplos usuários.

## Formas de execução previstas

| Forma | Recomendação | Público-alvo | Observação |
| --- | --- | --- | --- |
| Docker Compose | Recomendada para MVP | Equipe técnica e ambiente institucional | Isola serviços e reduz instalação manual |
| Instalação local com Python | Útil para desenvolvimento | Desenvolvedores | Exige instalar dependências manualmente |
| Executável único | Não recomendado agora | Uso individual/offline | Pode ser avaliado depois, com limitações |
| Servidor institucional | Recomendado para produção futura | CONOR/DGD/infraestrutura interna | Deve usar autenticação, backups e políticas de retenção |

## Por que contêiner é a melhor opção inicial

Um contêiner funciona como uma "caixa" com o ambiente técnico necessário para executar o sistema. Isso ajuda porque:

1. evita instalar várias bibliotecas diretamente no computador do arquivista;
2. reduz diferenças entre máquinas;
3. permite separar backend, banco de dados e armazenamento;
4. facilita backup e atualização;
5. permite implantação em infraestrutura interna sem serviços externos pagos;
6. preserva a possibilidade de auditoria e controle institucional.

## O que o Docker Compose deverá iniciar

A composição do MVP deverá iniciar, no mínimo:

1. API backend do sistema LED;
2. banco PostgreSQL;
3. volume persistente para arquivos enviados;
4. volume persistente para dados do banco.

Em etapa posterior, também deverá iniciar:

1. frontend web;
2. serviço de geração de relatórios, se for separado;
3. serviço de tarefas assíncronas, se necessário para PDFs grandes ou OCR.

## Como será para o arquivista

A experiência pretendida para o arquivista não deve envolver comandos técnicos no uso cotidiano. O fluxo esperado é:

1. a equipe técnica inicia ou disponibiliza o sistema;
2. o arquivista acessa o sistema pelo navegador;
3. o arquivista envia LED e tabela;
4. o arquivista revisa dados, executa regras, toma decisões e gera relatório.

## Como será para a equipe técnica no MVP

Na fase de protótipo, a equipe técnica poderá usar comandos como:

```bash
docker compose -f docker-compose.led.yml up --build
```

Esse comando deve ser executado na raiz do repositório e deverá iniciar os serviços do MVP quando Docker estiver instalado.

Como alternativa de desenvolvimento, dentro da pasta `backend`, será possível executar:

```bash
uvicorn app.main:app --reload
```

Esse modo é útil para desenvolvimento e testes, mas exige dependências Python instaladas.

## Decisão arquitetural

A decisão inicial é:

- **não** criar executável único agora;
- **sim** preparar execução por contêiner;
- **sim** permitir instalação local para desenvolvimento;
- **sim** manter possibilidade futura de empacotamento desktop, se houver necessidade institucional;
- **não** depender de serviços externos pagos;
- **não** enviar documentos para fora da infraestrutura autorizada por padrão.

## Próximo passo técnico

Para aproximar o protótipo do uso por arquivistas, o próximo passo é criar um frontend web simples ou uma página de protótipo que consuma os endpoints já existentes, permitindo testar análise estruturada sem usar comandos `curl`.
