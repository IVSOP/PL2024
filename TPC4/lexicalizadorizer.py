#!/usr/bin/env python3

import ply.lex as lex
import re
import sys

tokens = (
    'NUMBER',
	'SELECT',
	'FROM',
    'UPDATE',
    'DELETE',
    'CREATE',
    'WHERE',
    'SET',
    'DROP',
    'TABLE',
    'GREATER',
    'LESSER',
    'EQUALS',
    'COMMA',
    'SEMICOLON',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
	'WHITESPACE',
	'ESCAPE',
	'FIELD'
)

t_NUMBER = r'\d+(.\d+)?'
t_SELECT = r'SELECT'
t_FROM = r'FROM'
t_UPDATE = r'UPDATE'
t_DELETE = r'DELETE'
t_CREATE = r'CREATE'
t_WHERE = r'WHERE'
t_SET = r'SET'
t_DROP = r'DROP'
t_TABLE = r'TABLE'
t_GREATER = r'>'
t_LESSER = r'<'
t_EQUALS = r'='
t_COMMA = r','
t_SEMICOLON = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ESCAPE = r'\\'
t_FIELD = r'\w+'

def t_error(tok):
    print("Illegal character '%s'" % tok.value[0])
    tok.lexer.skip(1)

def t_WHITESPACE(tok):
    r'\s+'
    # make newline characters increment line count but still count as whitespace
    if '\n' in tok.value:
        tok.lexer.lineno += tok.value.count('\n')
    return tok

lexer = lex.lex()
lexer.input(sys.stdin.read())

for tok in lexer:
    print(tok)
