import ply.lex as lex
import ply.yacc as yacc
from ErrorChecker import *
from Parser import *
from PrintLog import *
from TambInstructions import *
import copy

def lex_test(file_path):
    sourceFile = file_path
    if sourceFile is not None:
        with open(sourceFile, 'r') as file:
            print("Entrando al lexer...")
            try:
                source = file.read()
            except EOFError as e:
                print(e)

            lexer = lex.lex()
            lexer.input(source)
            clone = lexer.clone()
            clone.input(source)
            error = Error_Checker()
            myprintLog = print_log()
            myTamb = TambInstructions()

            for token in clone:
                symbolTable.insertToken(token.type, token.value)

            #symbolTable.initial_table = copy.deepcopy(symbolTable.mytable)
            #instructions = myTamb.value()
            #print("instructions", myTamb.log)

            print("esta es mi tabla")
            symbolTable.printTable()

            if not main_checker():
                print("Voy a crear el parser")
                parser = yacc.yacc()
                parser.parse(source)

            #symbolTable.mytable = symbolTable.initial_table
            #symbolTable.printTable()
            #myTamb.log = instructions

            #print("instructions")
            #instructions = myTamb.value()
            #print(instructions)
            #instructions = myprintLog.value()
            #print(instructions)


            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")
            myprintLog.print()
            print(" \n *********** ERRORES DE COMPILACION *********** \n")
            error.print()

            print(" \n ******************* FIN ********************** \n")

def main_checker():
    if symbolTable.prinCounter != 1:
        print("Debe haber un solo main")
        error = Error_Generator(2, 1)
        error.Execute()
        return True
    else:
        return False

lex_test("test.pl0")