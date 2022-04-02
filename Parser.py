import ply.yacc as yacc
import os
import codecs
import re
from ErrorChecker import  *

import Statement_Module
from Lexical_analyzer import tokens
from sys import stdin
from Statement_Module import *



precedence = (
    ('right', 'ASSIGN', 'COMPARE'),
    ('left', 'NE'),
    ('left', 'LT', 'LTE', 'GT', 'GTE'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIVIDE_E'),
    ('left', 'MODULE'),
    ('left', 'EXPONENT'),
    ('left', 'LPARENT', 'RPARENT'),
)

#Variables for error detection
syntax_eror = False
semantic_error = False

def p_program(p):
	'''program : program prinDecl
			 | program functionDecl
			 | empty empty'''
	if p[1] != None:
		p[0] = [p[1], p[2]]
	else:
		p[0] = p[2]
	if p[0] != None:
		p[0] = simpleListBuilder().createListOfLists(p[0])
	print("Lista de instrucciones a ejecutar:")
	print(p[0])
	Principal(p[0])

def p_prinDecl(p):
	'''prinDecl : DEF PRIN LPARENT RPARENT LBRACKET statementList RBRACKET SEMICOLOM'''
	p[0] = ["PRIN", p[6]]

def p_functionDecl(p):
	'''functionDecl : DEF ID LPARENT varList RPARENT LBRACKET statementList RBRACKET SEMICOLOM'''
	line = p.lineno(2)
	symbolTable.mytable[p[2]]["scope"] = 'procedure block'
	p[0] = ["PROCEDURE", p[2], p[4], p[7], line]


def p_statementList1(p):
	'''statementList : statement '''
	p[0] = p[1]
	if p[0] != None:
		p[0] = simpleListBuilder().createListOfLists(p[0])

def p_statementList2(p):
	'''statementList : statementList statement '''
	p[0] = [p[1], p[2]]
	if p[0] != None:
		p[0] = simpleListBuilder().createListOfLists(p[0])


#SET
def p_statement1(p):
	'''statement : SET ID COMMA TRUE SEMICOLOM
    			| SET ID COMMA FALSE SEMICOLOM
    			| SET ID COMMA expression SEMICOLOM'''
	line = p.lineno(2)
	p[0] = ["SET", p[2], p[4], line]


#EXEC
def p_statement2(p):
	'''statement : EXEC ID LPARENT varList RPARENT SEMICOLOM'''
	line = p.lineno(2)
	p[0] = ["EXEC", p[2], p[4], line]


#TYPE
def p_statement3(p):
	'''statement : TYPE LPARENT ID RPARENT SEMICOLOM'''
	line = p.lineno(2)
	p[0] = ["TYPE", p[3], line]


#IF
def p_statement4(p):
	'''statement : IF conditionif LBRACKET statementList RBRACKET empty
                 | IF conditionif LBRACKET statementList RBRACKET ELSE LBRACKET statementList RBRACKET '''
	line = p.lineno(2)
	if len(p) == 10:
		p[0] = ["IF", p[2], line, p[4], p[8]]
	else:
		p[0] = ["IF", p[2], line, p[4], p[6]]


#FOR
def p_statement5(p):
	'''statement : FOR ID TO expression STEP NUMBER_I LBRACKET statementList RBRACKET
    			| FOR ID TO expression empty empty LBRACKET statementList RBRACKET'''

	line = p.lineno(2)
	p[0] = ["FOR", p[2], p[4], p[6], p[8], line]


#ENCASO
def p_statement6(p):
	'''statement : EC inCaseLista SN LBRACKET statementList RBRACKET FEC SEMICOLOM
	                 | EC ID inCaseListb SN LBRACKET statementList RBRACKET FEC SEMICOLOM'''
	line = p.lineno(2)
	if len(p) == 9:
		p[0] = ["ECa", p[2], p[5], line]
	else:
		p[0] = ["ECb", p[2], p[3], p[6], line]


#NE
def p_statement7(p):
	'''statement : SET ID DOT NEG SEMICOLOM'''
	line = p.lineno(2)
	p[0] = ["NE", p[2], line]


#TRUE - False
def p_statement8(p):
	'''statement : SET ID DOT T SEMICOLOM
    			 | SET ID DOT F SEMICOLOM'''
	line = p.lineno(2)
	p[0] = ["BOOLSET", p[2], p[4], line]


#abanico
def p_statement9(p):
	'''statement : ABANICO LPARENT A RPARENT SEMICOLOM
       			| ABANICO LPARENT B RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["ABANICO", p[3], line]


#vertical
def p_statement10(p):
	'''statement : VERTICAL LPARENT D RPARENT SEMICOLOM
       			| VERTICAL LPARENT I RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["VERTICAL", p[3], line]


#percutor
def p_statement11(p):
	'''statement : PERCUTOR LPARENT A empty RPARENT SEMICOLOM
       			| PERCUTOR LPARENT B empty RPARENT SEMICOLOM
       			| PERCUTOR LPARENT A B RPARENT SEMICOLOM
       			| PERCUTOR LPARENT D empty RPARENT SEMICOLOM
       			| PERCUTOR LPARENT I empty RPARENT SEMICOLOM
       			| PERCUTOR LPARENT D I RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["PERCUTOR", p[3], p[4], line]


#GOLPE
def p_statement12(p):
	'''statement : GOLPE LPARENT RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["GOLPE", line]


#VIBRATO
def p_statement13(p):
	'''statement : VIBRATO LPARENT NUMBER_I RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["VIBRATO", p[3], line]



#metronomo
def p_statement14(p):
	'''statement : METRONOMO LPARENT A COMMA NUMBER_I RPARENT SEMICOLOM
    		      | METRONOMO LPARENT D COMMA NUMBER_I RPARENT SEMICOLOM
    		      | METRONOMO LPARENT A COMMA NUMBER_F RPARENT SEMICOLOM
    		      | METRONOMO LPARENT D COMMA NUMBER_F RPARENT SEMICOLOM'''
	line = p.lineno(1)
	p[0] = ["METRONOMO", p[3], p[5], line]


#print
def p_statement15(p):
	'''statement : PRINT LPARENT printTextList RPARENT SEMICOLOM'''
	line = p.lineno(1)
	if isinstance(p[3], list):
		p[0] = ["PRINT", p[3], line]
	else:
		p[0] = ["PRINT", p[3], line]


def p_printTextList1(p):
	'''printTextList : printText'''
	p[0] = p[1]


def p_printTextList2(p):
	'''printTextList : printTextList COMMA printText'''

	p[0] = p[1] + "|$|" + p[3]


def p_printText(p):
	'''printText : printvar
				| STRING'''
	p[0] = p[1]
def p_printvar (p):
	'''printvar : ID
			| NUMBER_I
			| NUMBER_F
			| TRUE
			| FALSE'''
	p[0] = p[1]

def p_varList1(p):
	'''varList : var
				| empty'''
	p[0] = p[1]


def p_varList2(p):
	'''varList : varList COMMA var '''
	p[0] = p[1]+ p[3]


def p_var (p):
	'''var : ID
			| NUMBER_I
			| NUMBER_F
			| TRUE
			| FALSE'''
	p[0] = [p[1]]


def p_conditionif(p):
	'''conditionif : expression relation expression
				| TRUE
				| FALSE
				| ID
				| ID relation var'''
	if len(p) == 4:
		p[0] = p[1] + "|$|" + p[2] + "|$|" + p[3]
	else:
		p[0] = p[1]


def p_inCaseLista1(p):
	'''inCaseLista : inCasea '''
	p[0] = p[1]


def p_inCaseLista2(p):
	'''inCaseLista : inCaseLista inCasea'''
	p[0] = p[1] + p[2]


def p_inCasea(p):
	'''inCasea : CUANDO ID relation expression ET LBRACKET statementList RBRACKET
				|  CUANDO ID relation TRUE ET LBRACKET statementList RBRACKET
				|  CUANDO ID relation FALSE ET LBRACKET statementList RBRACKET'''
	line = p.lineno(1)
	p[0] = [[p[2], p[3], p[4], p[7], line]]


def p_inCaseListb1(p):
	'''inCaseListb : inCaseb '''
	p[0] = p[1]


def p_inCaseListb2(p):
	'''inCaseListb : inCaseListb inCaseb'''
	p[0] = p[1] + p[2]


def p_inCaseb (p):
	'''inCaseb : CUANDO relation expression ET LBRACKET statementList RBRACKET
				| CUANDO relation TRUE ET LBRACKET statementList RBRACKET
				| CUANDO relation FALSE ET LBRACKET statementList RBRACKET'''
	line = p.lineno(1)
	p[0] = [[p[2], p[3], p[6], line]]


def p_relation1(p):
	'''relation : COMPARE'''
	p[0] = p[1]


def p_relation2(p):
	'''relation : NE'''
	p[0] = p[1]


def p_relation3(p):
	'''relation : LT'''
	p[0] = p[1]


def p_relation4(p):
	'''relation : GT'''
	p[0] = p[1]


def p_relation5(p):
	'''relation : LTE'''
	p[0] = p[1]


def p_relation6(p):
	'''relation : GTE'''
	p[0] = p[1]


def p_expression1(p):
	'''expression : term'''
	p[0] = p[1]


def p_expression2(p):
	'''expression : addingOperator term'''
	p[0] = p[1] + "|$|" + p[2]


def p_expression3(p):
	'''expression : expression addingOperator term'''
	p[0] = p[1] + "|$|" + p[2] + "|$|" + p[3]


def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	p[0] = p[1]


def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	p[0] = p[1]


def p_term1(p):
	'''term : factor'''
	p[0] = p[1]

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	p[0] = p[1] + "|$|" +  p[2] + "|$|" +  p[3]


def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	p[0] = p[1]


def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	p[0] = p[1]


def p_multiplyingOperator3(p):
	'''multiplyingOperator : DIVIDE_E'''
	p[0] = p[1]


def p_factor1(p):
	'''factor : factorM'''
	p[0] = p[1]


def p_factor2(p):
	'''factor : factor MODULE factorM'''
	p[0] = p[1] + "|$|" +  p[2] + "|$|" +  p[3]


def p_factorM1(p):
	'''factorM : index'''
	p[0] = p[1]


def p_factorM2(p):
	'''factorM : factorM EXPONENT index'''
	p[0] = p[1] + "|$|" +  p[2] + "|$|" +  p[3]


def p_index1(p):
	'''index : NUMBER_I empty
			  | NUMBER_F empty
			  | addingOperator NUMBER_I
			  | addingOperator NUMBER_F
			  | addingOperator ID
			  | ID empty'''
	if p[2] != None:
		p[0] = p[1] + "|$|" +  p[2]
	else:
		p[0] = p[1]


def p_index2(p):
	'''index : LPARENT expression RPARENT'''
	p[0] = "("+ p[2] +")"


def p_empty(p):
	'''empty : '''
	pass

def p_error(p):
	#print ("Sintax Error in line", p.lineno)
	#print ("Sintax Error in line", p.lineno)
	if p == None:
		token = "end of file"
	else:
		token = f"{p.type}({p.value}) on line {p.lineno}"

	print(f"Syntax error: Unexpected {token}")
	error = Error_Checker()
	error.log_error(f"Syntax error: Unexpected {token}",2)


