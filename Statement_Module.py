import SymbolsTable
#from Arduino_code import *
from SymbolsTable import *
symbolTable = SymbolsTable()
stop = False


class Principal():
    def __init__(self, instructions):
        self.instructions = instructions
        if self.instructions != None:
            for i in self.instructions:
                if i[0] == "PRIN":
                    if i[1] != None:
                        self.runCode(i[1])

    def runCode(self, prinInstructions):
        print(prinInstructions)
        for i in prinInstructions:
            if i[0] == "SET":
                print("SET")
                if i[2] != 'True' and i[2] != 'False' and i[2][0] != '@':
                    print ("Operacion: ", i[2])
                    value = eval(i[2])
                    print(value)
                    result = symbolTable.insertValue(value, i[1], i[3])
                else:
                    print ("Boolean or ID: ", i[2])
                    result = symbolTable.insertValue(i[2], i[1], i[3])
                #Set(i[1], i[2], i[3], symbolTable.mytable, result)
                #Set(ID, TRUR/FALSE/expression, line,  table, result)
            elif i[0] == "EXEC":
                print("EXEC")
                #for j in self.instructions:
                 #   if j[1] == i[1]:
                        #Exec(i[2], j[2], j[3], symbolTable.mytable, i[3], j[4])
                        #Exec(varList, instruction[2], instruction[3], table, line, instruction[4])

            elif i[0] == "TYPE":
                print("TYPE")
                #Type(i[1], i[2], symbolTable.mytable)
                #Type(ID, line, table)

            elif i[0] == "IF":
                print("IF")
                #if If(i[1], symbolTable.mytable, i[2]).Comparison():
                  #If(conditionif, table, line])
                #    if i[3] != None: #i[3] = statementList If
                #        self.runCode(i[3])
                #elif i[4] != None: #i[4] = statementList Else
                 #   self.runCode(simpleListBuilder().createListOfLists(i[4]))

            elif i[0] == "FOR":
                print("FOR")
                #For(i[1], i[2], i[3], i[4], i[5], symbolTable.mytable)
                #For(ID, expression, Number_Id/empty, statementList, line, table)

            elif i[0] == "ECa":
                print("ECa")
                #ECa(i[1], i[2], symbolTable.mytable, i[3])
                #ECa(inCaseLista, statementList, table, line)

            elif i[0] == "ECb":
                print("ECb")
                #ECb(i[1], i[2], i[3], symbolTable.mytable, i[4])
                #ECb(ID, inCaseListb, statementList, table, line)

            elif i[0] == "NE":
                print("NE")
                #NE(i[1], i[2], symbolTable.mytable)
                #NE(i[1], i[2], table)

            elif i[0] == "BOOLSET":
                print("BOOLSET")
                #BOOLSET(i[1], i[2], i[3], symbolTable.mytable)
                #BOOLSET(ID, True/False, line, table)

            elif i[0] == "PRINT":
                print("PRINT")
                Print_(i[1], i[2], symbolTable) #Print_(printText/list, line, table)



class Print_:
    def __init__(self, value, line, myTable):
        self.value = value
        self.line = line
        self.table = symbolTable.mytable
        self.stringsList = symbolTable.getStringList()
        self.printLogger = ""
        #self.logger = PrintLog()
        self.printChecking()
        #self.logger.log_print.clean()
        #self.logger.log_print(self.printLogger)

        print("SE IMPRIMIRA EN LA CONSOLA -->  " + str(self.printLogger) + " DESDE LA LINEA " + str(self.line))

    def printChecking(self):

        for var in self.value:

            if isinstance(var, int):
                self.printLogger = self.printLogger + str(var)

            elif isinstance(validate_real_bool(var), bool):
                self.printLogger = self.printLogger + str(var)

            elif var in self.stringsList:

                self.printLogger = self.printLogger + var[1:-1]
            else:
                exist = False
                for i in self.table:
                    if i == var:
                        exist = True
                        break
                if exist:
                    self.printLogger = self.printLogger + str(self.table[i]["value"]) + " "
                else:
                    print ("error")


class simpleListBuilder:
    def createList(self, fingers):
        simpleList = []
        for i in fingers:
            if isinstance(i, list):
                simpleList += self.createList(i)
            else:
                simpleList.append(i)
        return simpleList

    def createListOfLists(self, lists):
        simpleList = []
        if isinstance(lists[0], list):
            for i in lists:
                if not isinstance(i[0], list):
                    sublists = []
                    for j in i:
                            sublists.append(j)
                    simpleList.append(sublists)
                else:
                    simpleList += self.createListOfLists(i)
        else:
            simpleList = [lists]
        return simpleList