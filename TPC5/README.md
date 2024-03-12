# TPC5: Analisador para máquina de vending

## 2024-03-12

## Autor:
- A100538
- Ivan Sérgio Rocha Ribeiro

## Resumo:
Usando o moduly ply.lex do python, criar um analisador que permita executar funcionalidades de uma máquina de vending:

- LISTAR: devolve uma lista dos itens disponíveis
- MOEDA \<moedas\>: estado de introdução de moedas. O formato das mesmas sera, por exemplo: `1c,2c,5c,10c,20c,50c,1e,2e.`, em que `.` significa o fim da sequencia, apos o qual sera mostrado o saldo atualizado.
- SELECIONAR \<numero\>: Seleciona o item dado um ID, removendo o saldo correspondente
- SAIR: termina, devolvendo o troco
