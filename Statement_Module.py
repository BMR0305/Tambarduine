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
                if i[2] != 'True' and i[2] != 'False' and len(i[2].split('|$|'))>1:
                    value = self.operation(i[2].split('|$|'), scope)

                elif i[2] == 'True':
                    value = True

                elif i[2] == 'False':
                    value = False

                else:
                    try:
                        value = int(i[2])
                    except ValueError:
                        value = i[2]

                exist = symbolTable.insertValue(value, i[1], i[3], scope)

                Set(i[1], value, i[3], symbolTable.mytable, exist, scope)
                    #Set(ID, TRUE/FALSE/expression, line,  table, exist, scope)

            elif i[0] == "EXEC":
                print("EXEC")
                for j in self.instructions:
                    if j[1] == i[1]:
                        Exec(i[2], j[2], j[3], i[1], symbolTable.mytable, i[3], j[4])
                        #Exec(parametros_exec, parametros_function, instruction, Id  table, line_exec, line_function)

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
                value = i[1].split('|$|')
                Print_(value, i[2], symbolTable, scope) #Print_(printText/list, line, table, scope)

    def operation(self, operations, scope):
        final_operation = ""
        for i in operations:
            try:
                int(i)
                final_operation = final_operation + i
            except ValueError:
                if i[0] == '@':
                    for var in symbolTable.mytable:
                        if var == i:
                            if symbolTable.mytable[var]["value"] != None and (symbolTable.mytable[var]["type"] == int or symbolTable.mytable[var]["type"] == float):
                                final_operation = final_operation + str(symbolTable.mytable[var]["value"])
                            else:
                                print("Error: Variable used in operation isn't valid")
                                return 0
                else:
                    final_operation = final_operation + i
        return eval(final_operation)

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
                type_ = None
                if type(self.value) == float:
                    type_ = int
                else:
                    type_ =  type(self.value)

                if self.table[self.id]["type"] == type_ \
                        and (self.scope == self.table[self.id]["scope"] or self.table[self.id]["scope"] == "Principal"):
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
                    if var == str(value) and (self.scope == self.table[var]["scope"] or self.table[var]["scope"] == "Principal"):
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
    def __init__(self, value, line, myTable, scope):
        self.value = value
        self.line = line
        self.table = symbolTable.mytable
        self.stringsList = symbolTable.getStringList()
        self.printLogger = ""
        self.scope = scope
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
                        if i == var and (self.scope == self.table[var]["scope"] or self.table[var]["scope"] == "Principal"):
                            exist = True
                            break
                    if exist:
                        self.printLogger = self.printLogger + str(self.table[i]["value"]) + " "
                    else:
                        print ("error")

class Exec:
    ##Exec(parametros_exec, parametros_function, instruction, Id  table, line_exec, line_function)
    def __init__(self, param_exec, param_fun, instructions, id, table, line_exec, line_fun):
        self.param_exec = param_exec
        self.instructions = instructions
        self.id = id
        self.param_fun = param_fun
        self.table = table
        self.line_exec = line_exec
        self.line_fun = line_fun

        if len(self.param_exec) == len(self.param_fun):
            if param_exec[0] != None:
                exist = False
                for i in param_fun:
                    for param in self.table:
                        if (param == i):
                            if self.table[param]["value"] != None:
                                #errorHandler = Generate_Error(15, self.lineP)
                                #errorHandler.Execute()
                                print("Error: Variable already declared")
                                exist = True
                                break
                    if exist:
                        break
                if not exist:
                    if self.validateParams(self.param_exec):
                        var = 0
                        while len(param_exec) != var:
                            self.table[param_fun[var]]["value"] = self.param_exec[var]
                            self.table[param_fun[var]]["type"] = type(self.param_exec[var])
                            self.table[param_fun[var]]["scope"] = self.id

                            var += 1

                        Principal(None).runCode(self.instructions, self.id)
                        for j in param_fun:
                            self.table[j]["value"] = None
                            self.table[j]["type"] = None
                            self.table[j]["scope"] = None

                        for k in self.table:
                            if k != "strings" and k != "cantidad" and self.table[k]["scope"] != "Principal":
                                self.table[k]["value"] = None
                                self.table[k]["type"] = None
                                self.table[k]["scope"] = None
            else:
                Principal(None).runCode(self.instructions, self.id)
                for k in self.table:
                    if k != "strings" and k != "cantidad" and self.table[k]["scope"] != "Principal":
                        self.table[k]["value"] = None
                        self.table[k]["type"] = None
                        self.table[k]["scope"] = None
        else:
            print("Error: Size of params in the declaration doesn't match with function params size")
            #errorHandler = Generate_Error(20, self.line)
            #errorHandler.Execute()

    def validateParams(self, params):
        errorFound = False
        param = 0
        for i in params:
            exist = True
            if i[0] == '@':
                for var in self.table:
                    if (var == i):
                        if self.table[var]["value"] != None:
                            exist = True
                            self.param_exec[param] = self.table[var]["value"]
                            break
                        else:
                            exist = False
            else:
                try:
                    self.param_exec[param] = int(i)
                except ValueError:
                    if i == "True":
                        self.param_exec[param] = True
                    elif i == "False":
                        self.param_exec[param] = False
                    else:
                        print("Error:The value of a param doesnt match any type")
            if not exist:
                #errorFound = True
                #errorHandler = Generate_Error(5, self.line)
                #errorHandler.Execute()
                print ("Error: Variable not found")
            param += 1
        if errorFound == False:
            return True
        else:
            return False

class simpleListBuilder:

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