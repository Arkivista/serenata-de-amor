# Protótipo local em navegador

O arquivo `prototipo-led-navegador.html` foi criado para ser aberto diretamente no navegador, sem Docker e sem instalação.

## Como abrir corretamente

Não digite apenas `samples/prototipo-led-navegador.html` na barra do navegador, porque alguns navegadores interpretam isso como pesquisa no Google.

Use uma destas opções:

### Opção 1 — Abrir pelo gerenciador de arquivos

1. Abra a pasta do projeto no seu computador.
2. Entre na pasta `samples`.
3. Dê duplo clique no arquivo `prototipo-led-navegador.html`.

### Opção 2 — Arrastar para o navegador

1. Abra a pasta `samples`.
2. Arraste o arquivo `prototipo-led-navegador.html` para uma janela do navegador.

### Opção 3 — Abrir pelo menu do navegador

1. No navegador, pressione `Ctrl+O` no Windows/Linux ou `Cmd+O` no macOS.
2. Selecione o arquivo `samples/prototipo-led-navegador.html`.

### Opção 4 — Usar endereço `file://`

Se quiser digitar o caminho na barra do navegador, use o caminho absoluto com `file://`.

Exemplo em Linux:

```text
file:///caminho/para/o/projeto/samples/prototipo-led-navegador.html
```

Exemplo em Windows:

```text
file:///C:/caminho/para/o/projeto/samples/prototipo-led-navegador.html
```

## Resultado esperado

A página deve abrir com o título:

```text
Protótipo local LED — teste sem contêiner
```

Depois, clique em:

```text
Executar análise no navegador
```

A página deve mostrar uma síntese com resultados `CONFORME` e `DIVERGENTE`.
