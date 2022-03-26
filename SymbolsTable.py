from Lexical_analyzer import *
from BooleanValidation import *
import pprint

#from Software.Semantic.Generate_Error import Generate_Error


class SymbolsTable:
    def __init__(self):
        self.mytable = {}
        self.prinCounter = 0
        self.ifexist = False
        self.stringList = []

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
            #errorHandler = Generate_Error(5, line)
            #errorHandler.Execute()
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
            print("NO BORRAR EL STRING PLS")
        else:
            pass

    def insertValue(self, value, name, line):
        exist = False
        for var in self.mytable:
            if var == name:
                if self.mytable[name]["value"] == None:
                    pass
                else:
                    exist = True
                    return True

        if not exist:
            t_value = value
            if isinstance(value, int):
                self.mytable[name]["value"] = t_value
                self.mytable[name]["type"] = int
            elif isinstance(validate_real_bool(value), bool):
                self.mytable[name]["value"] = t_value
                self.mytable[name]["type"] = bool
            elif isinstance(value, float):
                self.mytable[name]["value"] = t_value
                self.mytable[name]["type"] = float

            else:
                flag = True
                for var in self.mytable:
                    if var == str(value):
                        new_value = self.mytable[var]["value"]
                        self.mytable[name]["value"] = new_value
                        if isinstance(new_value, int):
                            self.mytable[name]["type"] = int
                            flag = False
                        if isinstance(new_value, float):
                            self.mytable[name]["type"] = float
                            flag = False
                        elif isinstance(validate_real_bool(new_value), bool):
                            self.mytable[name]["type"] = bool
                            flag = False

                if flag:
                    #errorHandler = Generate_Error(5, line)
                    #errorHandler.Execute()
                    print("error")
        return False

    def printTable(self):
        pprint.pprint(self.mytable)