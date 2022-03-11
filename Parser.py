import ply.yacc as yacc
import os
import codecs
import re
from Lexical_analyzer import tokens
from sys import stdin


precedence = (
    ('right', 'ASSING', 'COMPARE'),
    ('left','NE'),
    ('left','LT', 'LTE', 'GT', 'GTE'),
    ('left','PLUS', 'MINUS'),
    ('left','TIMES', 'DIVIDE', 'DIVIDE_E'),
	('left','MODULE'),
	('left', 'EXPONENT'),
    ('left','LPARENT', 'RPARENT'),
)

#intento de hacer la sintaxis

def consult_type(p):
	'''type LPARENT CONST RPARENT'''
	print('Imprimir tipo de la variable')

def bool_negation(p):
	'''SET const.NE'''
	print('cambiar valor de la variable')

def bool_true(p):
	'''SET const.T'''
	print('cambiar valor de la variable a true')

def bool_false(p):
	'''SET const.F'''
	print('cambiar valor de la variable a false')

def abanico_up(p):
	'''ABANICO(A)'''
	print("mover abanico desde arriba hacia abajo")

def abanico_down(p):
	'''ABANICO(B)'''
	print("mover abanico desde abajo hacia arriba")

def vertical_right(p):
	'''VERTICAL(D)'''
	print("Mover verticalmente hacia la derecha")

def vertical_left(p):
	'''VERTICAL(I)'''
	print("Mover verticalmente hacia la izquierda")

def percutor_D(p):
	'''PERCUTOR(D)'''
	print("Golpear pandereta por la derecha")

def percutor_I(p):
	'''PERCUTOR(I)'''
	print("Golpear pandereta por la izquierda")

def percutor_DI(DI):
	'''PERCUTOR(DI)'''
	print("Golpear pandereta por la derecha y la izquierda")

def percutor_A(p):
	'''PERCUTOR(A)'''
	print("Golpear pandereta por arriba")

def percutor_B(p):
	'''PERCUTOR(B)'''
	print("Golpear pandereta por abajo")

def percutor_AB(p):
	'''PERCUTOR(AB)'''
	print("Golpear pandereta por arriba y abajo")

def golpe(p):
	'''GOLPE()'''
	print("Golpear pandereta en el centro")

def vibrato(p):
	'''VIBRATO(number)'''
	print("Cantidad n de movimeintos verticales, n derecha y n izq")

def metronomo_A(p):
	'''METRONOMO(A, number)'''
	print("activa el metronomo con n pulsos por segundo")

def metronomo_D(p):
	'''METRONOMO(D, number)'''
	print("Desactiva el metronomo")

def println(p):
	'''println! (text);'''
	print('text') #ESTE PUNTO ES SUMAMENTE IMPORTANTE (debe concatenar)







def p_pgrogram(p):
    '''proram = block '''
    print("program")

def p_constDecl(p):
    '''SET constDecl, const constAssigmentList SEMMICOLOM''' #modificado

def p_constDeclEmpty(p):
    '''constDecl = empty'''

def p_constAssignmentList1(p):
	'''constAssignmentList : ID ASSIGN NUMBER'''
	print("constAssignmentList 1")

def p_constAssignmentList2(p):
	'''constAssignmentList : constAssignmentList COMMA ID ASSIGN NUMBER'''
	print("constAssignmentList 2")

def p_varDecl1(p):
	'''varDecl : VAR identList SEMMICOLOM'''
	print("varDecl 1")

def p_varDeclEmpty(p):
	'''varDecl : empty'''
	print("nulo")

def p_identList1(p):
	'''identList : ID'''
	print("identList 1")

def p_identList2(p):
	'''identList : identList COMMA ID'''
	print("identList 2")

def p_procDecl1(p):
	'''procDecl : procDecl PROCEDURE ID SEMMICOLOM block SEMMICOLOM'''
	print("procDecl 1")

def p_procDeclEmpty(p):
	'''procDecl : empty'''
	print("nulo")

def p_statement1(p):
	'''statement : ID UPDATE expression'''
	print("statement 1")

def p_statement2(p):
	'''statement : CALL ID'''
	print("statement 2")

def p_statement3(p):
	'''statement : BEGIN statementList END'''
	print("statement 3")

def p_statement4(p):
	'''statement : IF condition THEN statement'''
	print("statement 4")

def p_statement5(p):
	'''statement : WHILE condition DO statement'''
	print("statement 5")

def p_statementEmpty(p):
	'''statement : empty'''
	print("nulo")

def p_statementList1(p):
	'''statementList : statement'''
	print("statementList 1")

def p_statementList2(p):
	'''statementList : statementList SEMMICOLOM statement'''
	print("statementList 2")

def p_condition1(p):
	'''condition : ODD expression'''
	print("condition 1")

def p_condition2(p):
	'''condition : expression relation expression'''
	print("condition 2")

def p_relation1(p):
	'''relation : ASSIGN'''
	print("relation 1")

def p_relation2(p):
	'''relation : NE'''
	print("relation 2")

def p_relation3(p):
	'''relation : LT'''
	print("relation 3")

def p_relation4(p):
	'''relation : GT'''
	print("relation 4")

def p_relation5(p):
	'''relation : LTE'''
	print("relation 5")

def p_relation6(p):
	'''relation : GTE'''
	print("relation 6")

def p_expression1(p):
	'''expression : term'''
	print("expresion 1")

def p_expression2(p):
	'''expression : addingOperator term'''
	print("expresion 2")

def p_expression3(p):
	'''expression : expression addingOperator term'''
	print("expresion 3")

def p_addingOperator1(p):
	'''addingOperator : PLUS'''
	print("addingOperator 1")

def p_addingOperator2(p):
	'''addingOperator : MINUS'''
	print("addingOperator 1")

def p_term1(p):
	'''term : factor'''
	print("term 1")

def p_term2(p):
	'''term : term multiplyingOperator factor'''
	print("term 1")

def p_multiplyingOperator1(p):
	'''multiplyingOperator : TIMES'''
	print("multiplyingOperator 1")

def p_multiplyingOperator2(p):
	'''multiplyingOperator : DIVIDE'''
	print("multiplyingOperator 2")

def p_factor1(p):
	'''factor : ID'''
	print("factor 1")

def p_factor2(p):
	'''factor : NUMBER'''
	print("factor 1")

def p_factor3(p):
	'''factor : LPARENT expression RPARENT'''
	print ("factor 1")

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
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Has escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = '/Users/Usuario/Documents/GitHub/Tambarduine/Tests/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test,"r","utf-8")
cadena = fp.read()
fp.close()

parser = yacc.yacc()
result = parser.parse(cadena)

print (result)
