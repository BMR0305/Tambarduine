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
                # Type(ID, line, table)
                Type(i[1], i[2], symbolTable.mytable)

            elif i[0] == "IF":
                if i[1] != 'True' and i[1] != 'False' and len(i[1].split('|$|'))>1:
                    value = self.operation(i[1].split('|$|'), scope)

                elif i[1] == 'True':
                    value = True

                elif i[1] == 'False':
                    value = False

                else:
                    try:
                        value = int(i[1])
                    except ValueError:
                        value = i[1]

                If(value, i[2], i[3], i[4], symbolTable.mytable, scope)

            elif i[0] == "FOR":
                exist = False
                for var in symbolTable.mytable:
                    if var == i[1]:
                        if symbolTable.mytable[i[1]]["value"] == None:
                            pass
                        else:
                            exist = True
                if not exist:
                    symbolTable.mytable[i[1]]["value"] = 1
                    symbolTable.mytable[i[1]]["type"] = int
                    symbolTable.mytable[i[1]]["scope"] = scope

                For(i[1], i[2], i[3], i[4], i[5], symbolTable.mytable)
                #For(ID, expression, Number_Id/empty, statementList, line, table)

            elif i[0] == "ECa":
                # EC(value, line, statementListEC, statementListSN)
                flag = False
                print(i[1])
                if len(i[1]) == 1:
                    expression = [i[1][0][0], i[1][0][1], i[1][0][2]]
                    value = self.operation(expression, scope)
                    if value == True:
                        flag = value
                        self.runCode(i[1][0][3], scope)

                else:
                    for j in i[1]:
                        expression=[j[0], j[1], j[2]]
                        value = self.operation(expression, scope)
                        if value == True:
                            flag = value
                            self.runCode(i[1][0][3], scope)
                if not flag:
                    self.runCode(i[2], scope)


            elif i[0] == "ECb":
                # EC(value, line, statementListEC, statementListSN)
                print("ecb")
                for j in i[2]:
                    expression = [i[1], j[0], j[1]]

                    value = self.operation(expression, scope)
                    print(value)
                    if value:
                        print("mi",i[2])
                        self.runCode(j[2], scope)
                        break
                if value == False:
                    self.runCode(i[3], scope)

            elif i[0] == "NE":
                exist = False
                for var in symbolTable.mytable:
                    if var == i[1]:
                        if symbolTable.mytable[i[1]]["value"] == None:
                            pass
                        else:
                            exist = True
                if exist and symbolTable.mytable[i[1]]["type"] == bool:
                    if symbolTable.mytable[i[1]]["value"] == True:
                        symbolTable.mytable[i[1]]["value"] = False

                    elif symbolTable.mytable[i[1]]["value"] == False:
                        symbolTable.mytable[i[1]]["value"] = True

            elif i[0] == "BOOLSET":
                exist = False
                for var in symbolTable.mytable:
                    if var == i[1]:
                        if symbolTable.mytable[i[1]]["value"] == None:
                            pass
                        else:
                            exist = True
                if exist and symbolTable.mytable[i[1]]["type"] == bool:
                    if i[2] == 'T':
                        symbolTable.mytable[i[1]]["value"] = True

                    elif i[2] == 'F':
                        symbolTable.mytable[i[1]]["value"] = False



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
                            if symbolTable.mytable[var]["value"] != None and \
                                    (symbolTable.mytable[var]["type"] == int or symbolTable.mytable[var]["type"] == float) and \
                                    (scope == symbolTable.mytable[var]["scope"] or "Principal" == symbolTable.mytable[var]["scope"]):

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

class Type:
    def __init__(self, ID, line, table):
        self.ID = ID
        self.line = line
        self.table = table

        flag = False
        for var in self.table:
            if var == self.ID:
                if self.table[ID]["type"] != None:
                    flag = True
                    break
        if flag:
            print("Variable",self.ID,"is:",(str(self.table[ID]["type"])).replace("<class '", "").replace("'>",""))
        else:
            print("Error: Variable not found in line" , self.line)

# (IF, conditionif, line, statementListIf, empty)
# (IF, conditionif, line, statementListIf, statementListElse)
class If:
    def __init__(self, conditionif, line, statementListIf, statementListElse, table, scope):
        self.conditionif = conditionif
        self.line = line
        self.statementListIf = statementListIf
        self.statementListElse = statementListElse
        self.table = table
        self.scope = scope

        if self.conditionif:
            Principal.runCode(self, self.statementListIf, self.scope)


        elif not self.conditionif and self.statementListElse != None:
            Principal.runCode(self, self.statementListElse, self.scope)

class For:
    # For(ID, expression, Number_Id/empty, statementList, line, table)
    # for @var1 to x Step 1
    def __init__(self, ID, max, step, statementList, line, table):
        self.ID = ID
        self.max = int(max)
        self.statementList = statementList
        self.line = line
        self.table = table
        try:
            self.step = int(step)
        except TypeError:
            self.step = 1


        if int(self.table[self.ID]["value"]) <= self.max:
            self.runFor()

    def runFor(self):
        i = True
        while i:
            Principal(None).runCode( self.statementList, "For")
            self.table[self.ID]["value"] = int(self.table[self.ID]["value"]) + self.step
            if self.max < int(self.table[self.ID]["value"]):
                i = False

        if self.table[self.ID]["scope"] == "For":
            self.table[self.ID]["value"] = None
            self.table[self.ID]["type"] = None
            self.table[self.ID]["scope"] = None

#class EC:
 #   def __init__(self, conditionEC, line):



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