# Calculadora de Pace

Programa de terminal feito em Python para calcular pace e tempos previstos de corrida.

O objetivo é informar uma distância e um tempo, ou uma distância e um pace, para receber os cálculos de forma rápida. Além do resultado principal, o programa cria uma tabela com os tempos previstos para 200 m, 400 m, 600 m, 800 m e 1000 m.

Também é possível acrescentar uma distância personalizada à tabela.

## Como executar

No terminal, entre na pasta do projeto e execute:

```bash
python main.py
```

## Formatos de entrada

- Tempo: `HH"MM"SS` — por exemplo, `01"23"45`.
- Distância: `KM"METROS` — por exemplo, `2"500` para 2,5 km ou `0"400` para 400 m.
- Pace: `MM"SS` por quilômetro — por exemplo, `05"30`.

## Próxima versão

Esta primeira versão foi criada no terminal para praticar os fundamentos de Python: funções, validação de entrada, cálculos e organização do código em arquivos.

A próxima versão terá uma interface gráfica para o usuário, feita com PySide6. A ideia é substituir as perguntas do terminal por campos de entrada, botões e uma tabela visual de resultados, mantendo a lógica de cálculo que já existe neste projeto.
