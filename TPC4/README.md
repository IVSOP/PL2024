# TPC4: Analisador Léxico SQL

## 2024-03-05

## Autor:
- A100538
- Ivan Sérgio Rocha Ribeiro

## Resumo:
Usando o moduly ply.lex do python, criar um analisador que permita, pelo menos, identificar os simbolos em `SELECT id, nome, salario FROM empregados WHERE salario >= 820`

Para tal, foi criado o script `lexicalizadorizer.py`, que identifica varios tokens de SQL (SELECT, FROM, TABLE, ...) e tambem outros mais gerais, como valores, <, >, =, whitespace, etc, utilizando regex.
