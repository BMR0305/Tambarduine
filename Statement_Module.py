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
                        self.runCode(i[1], "Principal")

    def runCode(self, instructions, scope):
        print(instructions)
        for i in instructions:
            if i[0] == "SET":
                if i[2] != 'True' and i[2] != 'False' and str(i[2][0]) != '@':
                    value = eval(i[2])

                elif i[2] == 'True':
                    value = True

                elif i[2] == 'False':
                    value = False

                else:
                    value = i[2]

                exist = symbolTable.insertValue(value, i[1], i[3], scope)

                Set(i[1], value, i[3], symbolTable.mytable, exist, scope)
                    #Set(ID, TRUE/FALSE/expression, line,  table, exist, scope)

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
                value = i[1].split('$')
                Print_(value, i[2], symbolTable) #Print_(printText/list, line, table)


class Set:
                # Set(ID, TRUE/FALSE/expression, line,  table, exist)
    def __init__(self, id, value, line, symbol_table, exist, scope):
        self.id = id
        self.value = value
        self.line = line
        self.table = symbol_table
        self.exist = exist
        self.scope = scope

        #EXISTANCE ANALYSIS

        if self.exist:
            if isinstance(self.value, int) or isinstance(self.value, bool) or isinstance(self.value, float):
                if type(self.table[self.id]["value"]) == type(self.value):
                    self.table[self.id]["value"] = self.value
                    print("SE HA REGISTRADO EL SET  " + self.id + " CON EL VALOR DE " + str(
                        self.value) + " EN LA LINEA " + str(self.line))

                else:
                    #errorHandler=Generate_Error(15, self.line)
                    #errorHandler.Execute()
                    print("Error: Can't change initial type in line" , line)

            else:
                flag = True
                for var in self.table:
                    if var == str(value) and (scope == self.table[var]["scope"] or self.table[var]["scope"] == "Principal"):
                        if (self.table[self.value]["type"]) != (self.table[self.id]["type"]):
                            #errorHandler = Generate_Error(4, self.line)
                            #errorHandler.Execute()
                            print("Error: Variable type unmatch in line", line)
                            flag = False
                            break

                        else:
                            self.table[self.id]["value"] = self.table[self.value]["value"]
                            flag = False
                            print("SE HA REGISTRADO EL SET  " + self.id + " CON EL VALOR DE " + str(
                                self.value) + " EN LA LINEA " + str(self.line))
                            break

                if flag:
                    #errorHandler = Generate_Error(5, self.line)
                    #errorHandler.Execute()
                    print("Error: Variable not found in line" , line)



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
            try:
                int(var)
                self.printLogger = self.printLogger + str(var) + " "

            except ValueError:
                if var in self.stringsList:
                    self.printLogger = self.printLogger + var[1:-1] + " "
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