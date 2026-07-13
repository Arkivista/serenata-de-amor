# Backend do Sistema de Apoio à Análise de LEDs

Este backend é a base técnica inicial do MVP. Ele ainda não implementa upload, extração, motor de regras ou relatórios.

## O que existe agora

- Aplicação FastAPI mínima.
- Endpoint `/health` para verificar se a API iniciou.
- Configuração por variáveis de ambiente.
- IA desativada por padrão.
- Interface desacoplada para futuras sugestões de IA, sem poder decisório.
- Testes unitários básicos de configuração e contrato de IA.

## Como executar futuramente

Na pasta `backend`, após instalar as dependências em ambiente virtual:

```bash
uvicorn app.main:app --reload
```

Resultado esperado: a API deve iniciar e expor `/health`.

## Como testar

Na pasta `backend`, com as dependências de desenvolvimento instaladas:

```bash
PYTHONPATH=. pytest
```

Resultado esperado: todos os testes passam.
