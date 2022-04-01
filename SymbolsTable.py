from Lexical_analyzer import *
from BooleanValidation import *
import pprint
import ErrorGenerator

#from Software.Semantic.Generate_Error import Generate_Error


class SymbolsTable:
    def __init__(self):
        self.mytable = {}
        self.prinCounter = 0
        self.ifexist = False
        self.stringList = []
        self.initial_table = {}

    def Clean(self):
        self.mytable = {}
        self.prinCounter = 0

    def getValue(self, name, line):
        found = False
        for key in self.mytable:
            if key == name:
                found = True
                return self.mytable[name]["value"]
            else:
                found = False
        if not found:
            errorHandler = ErrorGenerator(5, line)
            errorHandler.Execute()
            print("error")
    def getStringList(self):
        return self.stringList

    def insertToken(self, key, name):
        key = str(key)
        if key == "ID":
            exist = False
            for var in self.mytable:
                if var == name:
                    exist = True
                    break
            if not exist:
                self.mytable[name] = {
                    "type": None,
                    "value": None,
                    "scope": None,
                }

        elif key == "PRIN":
            self.prinCounter += 1
            self.mytable[name] = {
                "cantidad": self.prinCounter,
                "scope": "Principal block",
            }
        elif key == "STRING":
            self.stringList = self.stringList + [name]
            self.mytable["strings"] = self.stringList
        else:
            pass

    def insertValue(self, value, name, line, scope):
        exist = False
        for var in self.mytable:
            if var == name:
                if self.mytable[name]["value"] == None:
                    pass
                else:
                    return True

        if not exist:
            if (isinstance(value, int) or isinstance(value, bool) or isinstance(value, float)):
                self.mytable[name]["value"] = value
                if self.mytable[name]["type"] == float:
                    self.mytable[name]["type"] = int
                else:
                    self.mytable[name]["type"] = type(value)
                self.mytable[name]["scope"] = scope

            else:
                flag = True
                for var in self.mytable:
                    if var == str(value) and (scope == self.mytable[var]["scope"] or self.mytable[var]["scope"] == "Principal"):
                        new_value = self.mytable[var]["value"]
                        self.mytable[name]["value"] = new_value
                        if self.mytable[name]["type"] == float:
                            self.mytable[name]["type"] = int
                        else:
                            self.mytable[name]["type"] = self.mytable[var]["type"]
                        self.mytable[name]["scope"] = scope
                        flag = False



                if flag:
                    errorHandler = ErrorGenerator(5, line)
                    errorHandler.Execute()
                    print("Error: Variable not found in line", line)
        return False

    def printTable(self):
        pprint.pprint(self.mytable)