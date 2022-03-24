import ply.yacc as yacc
import os
import codecs
import re
from Lexical_analyzer import tokens
from sys import stdin

global in_global
in_global = False

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


def p_program(p):
    '''program : block '''
    # p[0] = program(p[1], "program")
    print("program")

def p_block(p):
	'''block : functionDecl block
			 | empty'''
	print("block")

def p_functionDecl(p):
	'''functionDecl : DEF PRIN LPARENT RPARENT LBRACKET statementList RBRACKET
	         | DEF ID LPARENT varList RPARENT LBRACKET statementList RBRACKET'''
	print("functionDecl")

def p_statementList1(p):
	'''statementList : statement '''
	print("statementList1")

def p_statementList2(p):
	'''statementList : statementList statement '''
	print("statementList2")

#SET
def p_statement1(p):
    '''statement : SET ID COMMA NUMBER_I SEMICOLOM
    			| SET ID COMMA NUMBER_F SEMICOLOM
    			| SET ID COMMA TRUE SEMICOLOM
    			| SET ID COMMA FALSE SEMICOLOM'''
    print("statement 1")

#EXEC
def p_statement2(p):
    '''statement : EXEC ID LPARENT varList RPARENT SEMICOLOM'''
    print("statement 2")

#TYPE
def p_statement3(p):
    '''statement : TYPE LPARENT ID RPARENT SEMICOLOM'''
    print("statement 3")

#IF
def p_statement4(p):
    '''statement : IF conditionif LBRACKET statementList RBRACKET
                 | IF conditionif LBRACKET statementList RBRACKET ELSE LBRACKET statementList RBRACKET '''
    print("statement 4")

#FOR
def p_statement5(p):
    '''statement : FOR ID TO var STEP NUMBER_I LBRACKET statementList RBRACKET
    			| FOR ID TO var STEP LBRACKET statementList RBRACKET'''
    print("statement 5")

#ENCASO
def p_statement6(p):
	'''statement : EC inCaseLista SN LBRACKET statementList RBRACKET FEC SEMICOLOM
	                 | EC ID inCaseListb SN LBRACKET statementList RBRACKET FEC SEMICOLOM'''
	print("statement 6")

#NE
def p_statement7(p):
    '''statement : SET ID DOT NEG SEMICOLOM'''
    print('statement 7')

#TRUE - False
def p_statement8(p):
    '''statement : SET ID DOT T SEMICOLOM
    			 | SET ID DOT F SEMICOLOM'''
    print('statement 8')

#abanico
def p_statement9(p):
    '''statement : ABANICO LPARENT A RPARENT SEMICOLOM
       			| ABANICO LPARENT B RPARENT SEMICOLOM'''
    print("statement 9")

#vertical
def p_statement10(p):
    '''statement : VERTICAL LPARENT D RPARENT SEMICOLOM
       			| VERTICAL LPARENT I RPARENT SEMICOLOM'''
    print("statement 10")


#percutor
def p_statement11(p):
    '''statement : PERCUTOR LPARENT A RPARENT SEMICOLOM
       			| PERCUTOR LPARENT B RPARENT SEMICOLOM
       			| PERCUTOR LPARENT A B RPARENT SEMICOLOM
       			| PERCUTOR LPARENT D RPARENT SEMICOLOM
       			| PERCUTOR LPARENT I RPARENT SEMICOLOM
       			| PERCUTOR LPARENT D I RPARENT SEMICOLOM'''

    print("statement 11")


#GOLPE
def p_statement12(p):
    '''statement : GOLPE LPARENT RPARENT SEMICOLOM'''
    print('statement 12')

#VIBRATO
def p_statement13(p):
    '''statement : VIBRATO LPARENT NUMBER_I RPARENT SEMICOLOM'''
    print('statement 13')


#metronomo
def p_statement14(p):
    '''statement : METRONOMO LPARENT A COMMA NUMBER_I RPARENT SEMICOLOM
    		      | METRONOMO LPARENT D COMMA NUMBER_I RPARENT SEMICOLOM
    		      | METRONOMO LPARENT A COMMA NUMBER_F RPARENT SEMICOLOM
    		      | METRONOMO LPARENT D COMMA NUMBER_F RPARENT SEMICOLOM'''
    print('statement 14')

#print
def p_statement15(p):
    '''statement : PRINT LPARENT printTextList RPARENT SEMICOLOM'''
    print('statement 15')

def p_printTextList1(p):
	'''printTextList : printText'''
	print("printTextList1")

def p_printTextList2(p):
	'''printTextList : printTextList COMMA printText'''
	print("printTextList2")

def p_printText(p):
	'''printText : factor
					| STRING'''
	print ('printText')

def p_varList1(p):
	'''varList : var
				| empty'''
	print("varList1")

def p_varList2(p):
	'''varList : varList COMMA var '''
	print("varList2")

def p_var (p):
	'''var : ID
			| NUMBER_I
			| NUMBER_F
			| TRUE
			| FALSE'''
	print("var")

def p_conditionif(p):
	'''conditionif : expression relation expression
				| TRUE
				| FALSE
				| ID'''
	print("conditionif")

def p_inCaseLista1(p):
	'''inCaseLista : inCasea '''
	print("inCaseLista1")

def p_inCaseLista2(p):
	'''inCaseLista : inCaseLista inCasea'''
	print("inCaseLista2")

def p_inCasea(p):
	'''inCasea : ID relation expression'''
	print("inCasea")

def p_inCaseListb1(p):
	'''inCaseListb : inCaseb '''
	print("inCaseListb1")

def p_inCaseListb2(p):
	'''inCaseListb : inCaseListb inCaseb'''
	print("inCaseListb2")

def p_inCaseb (b):
	'''inCaseb : relation expression'''
	print("inCaseb")

def p_relation1(p):
	'''relation : COMPARE'''
	print ("relation 1")

def p_relation2(p):
	'''relation : NE'''
	print ("relation 2")

def p_relation3(p):
	'''relation : LT'''
	print ("relation 3")

def p_relation4(p):
	'''relation : GT'''
	print ("relation 4")

def p_relation5(p):
	'''relation : LTE'''
	print ("relation 5")

def p_relation6(p):
	'''relation : GTE'''
	print ("relation 6")

def p_expression1(p):
	'''expression : term'''
	print ("expresion 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	print ("expresion 2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print ("expresion 3")

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print ("addingOperator 1")

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print ("addingOperator 2")

def p_term1(p):
	'''term : factor'''
	print ("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print ("term 2")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print ("multiplyingOperator 1")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print ("multiplyingOperator 2")

def p_factor1(p):
	'''factor : ID'''
	print ("factor 1")

def p_factor2(p):
	'''factor : NUMBER_I
			  | NUMBER_F'''
	print ("factor 2")

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print ("factor 3")

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print ("Error de sintaxis ", p)
	#print "Error en la linea "+str(p.lineno)

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]


directorio = '/Users/Lenovo/Documents/GitHub/Tambarduine/Tests/Test_arduino/'
archivo = buscarFicheros(directorio)
test = directorio + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print(result)
