#!/usr/bin/env python3

import ply.lex as lex
import sys
from tabulate import tabulate

def print_saldo(saldo):
    saldo_cent = saldo * 100
    euros = saldo_cent // 100 # int division
    cents = saldo_cent % 100
    print(f"Saldo: {str(saldo)} ({str(euros)}e{str(cents)}c)")

def print_troco(saldo):
	res = []
	coins = [("2e", 200), ("1e", 100), ("50c", 50), ("20c", 20), ("10c", 10), ("5c", 5), ("2c", 2), ("1c", 1)]
	coin_iter = 0
	while saldo > 0:
		curr_coin_type  = coins[coin_iter]
		n_coin = saldo // curr_coin_type[1]
		saldo = saldo % curr_coin_type[1]
		if (n_coin > 0):
			res.extend([curr_coin_type[0]] * n_coin)
		coin_iter = coin_iter + 1
	print("TROCO: " + res)

produtos = [
    {"cod": "A1", "nome": "agua", "quant": 4, "preco": 0.50},
	{"cod": "A2", "nome": "salame de chocolate", "quant": 5, "preco": 0.85},
	{"cod": "A3", "nome": "explosivo termonuclear", "quant": 1, "preco": 999999999.999},
	{"cod": "A4", "nome": "sandes de presunto",  "quant": 7,"preco": 1.50},
	{"cod": "A5", "nome": "porsche 911 gt3 rs", "quant": 2, "preco": 315000.000},
	{"cod": "A6", "nome": "kitkat", "quant": 3, "preco": 0.75}
]

def find_produto(cod):
	for prod in produtos:
		if prod["cod"] == cod:
			return prod
	return None


tokens = [
    "INIT_COIN",
    "COIN",
    "COMMA",
    "END_COIN"
    "LIST"
    "SELECT",
    "NUMBER"
    "EXIT",
]

states = (
    ('selecionar', 'exclusive'),
    ('moeda', 'exclusive')
)

t_ignore = "\n\t "
def t_error(t):
    print("Erro no caracter " + t.value[0])
    t.lexer.skip(1)

t_moeda_ignore = t_ignore + ','
def t_moeda_error(t):
    print("Moeda: erro no caracter " + t.value[0])
    t.lexer.skip(1)

t_selecionar_ignore = t_ignore
def t_selecionar_error(t):
    print("Selecionar: erro no caracter " + t.value[0])
    t.lexer.skip(1)

def t_INIT_COIN(t):
    r'^MOEDA'
    t.lexer.begin('moeda')

# nome do estado ta no nome da funcao
def t_moeda_COIN(t):
    r'(1c|5c|10c|20c|50c|1e|2e)'
    moeda = int(t.value[:-1])
    if t.value[-1] == 'c':
        moeda /= 100
    t.lexer.saldo += moeda

def t_moeda_END_COIN(t):
    r'\.$'
    print_saldo(t.lexer.saldo)
    t.lexer.begin("INITIAL")

def t_LISTAR(t):
	r'^LISTAR$'
	table = []
	for prod in produtos:
        # print(f"{i}: {prod} ({preco})")
		table.append(list(prod.values()))
	print(tabulate(table, headers=["cod", "nome", "quant", "preco"], numalign="right"))

def t_SELECT(t):
	r'^SELECIONAR'
	t.lexer.begin("selecionar")

def t_selecionar_NUMBER(t):
	r'[A-Z]\d+$'
	prod = find_produto(t.value)
	if (prod is None):
		print("Produto nao existe")
	elif prod["quant"] == 0:
		print("Produto esgotado")
	elif t.lexer.saldo >= prod["preco"]:
		print("SELECIONADO " + prod["nome"])
		t.lexer.saldo -= prod["preco"]
		prod["quant"] -= 1
		print_saldo(t.lexer.saldo)
	else:
		print("SALDO INSUFICIENTE")
	t.lexer.begin("INITIAL")
    

def t_EXIT(t):
    r'^SAIR'
    print_troco(t.lexer.saldo)
    exit(0)


lexer = lex.lex()
lexer.saldo = 0

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)
