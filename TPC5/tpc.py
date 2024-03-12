#!/usr/bin/env python3

import ply.lex as lex
import sys

def print_saldo(saldo):
    euros = saldo // 100 # int division
    cents = saldo % 100
    print(f"Saldo: {str(saldo)} ({str(euros)}e{str(cents)}c)")

produtos = [
    ("agua", 50),
	("salame de chocolate", 85),
	("explosivo termonuclear", 999999999999),
	("sandes de presunto", 150),
	("porsche 911 gt3 rs", 315000000),
	("kitkat", 75)
]

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
    if t.value[-1] == 'e':
        moeda *= 100
    t.lexer.saldo += moeda

def t_moeda_END_COIN(t):
    r'\.$'
    print_saldo(t.lexer.saldo)
    t.lexer.begin("INITIAL")

def t_LISTAR(t):
    r'^LISTAR$'
    i = 0
    for (prod, preco) in produtos:
        print(f"{i}: {prod} ({preco})")
        i += 1

def t_SELECT(t):
	r'^SELECIONAR'
	t.lexer.begin("selecionar")

def t_selecionar_NUMBER(t):
	r'\d+$'
	prod, preco = produtos[int(t.value)]
	if t.lexer.saldo >= preco:
		print("SELECIONADO " + prod)
		t.lexer.saldo -= preco
		print_saldo(t.lexer.saldo)
	else:
		print("SALDO INSUFICIENTE")
		t.lexer.begin("INITIAL")
    

def t_EXIT(t):
    r'^SAIR'
    print_saldo(t.lexer.saldo) # age como o troco
    exit(0)


lexer = lex.lex()
lexer.saldo = 0

for line in sys.stdin:
    lexer.input(line)
    for tok in lexer:
        print(tok)
