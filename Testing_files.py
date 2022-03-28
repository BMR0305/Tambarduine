import ply.lex as lex
import ply.yacc as yacc
from ErrorChecker import *
from Parser import *

def lex_test():
    sourceFile = "test.pl0"
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
            error = ErrorChecker()

            for token in clone:
                symbolTable.insertToken(token.type, token.value)

            print("esta es mi tabla")
            symbolTable.printTable()

            if not main_checker():
                print("Voy a crear el parser")
                parser = yacc.yacc()
                parser.parse(source)



            symbolTable.printTable()
            print("Saliendo del parser...")
            print("TERMINE DE COMPILAR")
            print(" \n *********** ERRORES DE COMPILACION *********** \n")
            error.print()

            print(" \n ******************* FIN ********************** \n")

def main_checker():
    if symbolTable.prinCounter != 1:
        print("Debe haber un solo main")
        return True
    else:
        return False

lex_test()