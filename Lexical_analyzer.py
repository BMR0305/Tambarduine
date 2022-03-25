import ply.lex as lex
import re
import codecs
import os
import sys
import Reserved_words
import Tokens

tokens = Tokens.tokens
reserved = Reserved_words.reserved

tokens = tokens + reserved

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EXPONENT = r'\*\*'
t_DIVIDE_E = r'//'
t_MODULE = r'%'
t_ASSIGN = r'='
t_COMPARE = r'=='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_COMMA = r','
t_SEMICOLOM= r';'
t_DOT = r'\.'
t_SET = r'SET'
t_TRUE = r'True'
t_FALSE = r'False'
t_T = r'T'
t_F = r'F'
t_TYPE = r'type'
t_ABANICO = r'Abanico'
t_VERTICAL = r'Vertical'
t_PERCUTOR = r'Percutor'
t_GOLPE = r'Golpe'
t_VIBRATO = r'Vibrato'
t_METRONOMO = r'Metronomo'
t_A = r'A'
t_B = r'B'
t_D = r'D'
t_I = r'I'
t_PRINT = r'println!'
t_FOR = r'for'
t_TO = r'to'
t_STEP = r'Step'
t_IF = r'If'
t_ELSE = r'Else'
t_EC = r'EnCaso'
t_CUANDO = r'Cuando'
t_ET = r'EnTos'
t_SN = r'SiNo'
t_FEC = r'Fin-EnCaso'
t_DEF = r'Def'
t_PRIN = r'Principal'
t_EXEC = r'Exec'
t_NEG = r'Neg'



def t_ID(t):
    r'[@][a-zA-Z0-9_?][a-zA-Z0-9_?][a-zA-Z0-9_?]*'
    if t.value.upper() in reserved:
        t.value = t.value.upper
        t.type = t.value
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_COMMENT (t):
    r'\#.*'
    pass

def t_NUMBER_I (t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NUMBER_F (t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t
def t_STRING (t):
    r'".*"'

def t_error (t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



#analizer = lex.lex()


