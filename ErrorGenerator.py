import ErrorChecker
import Parser

class ErrorGenerator:
    def __init__(self, code, line=0):
        self.code = code
        self.line = line
        self.error = ErrorChecker()

    def Execute(self):
        if self.code == 0:
            msg = "Syntax is incorrect"
            Parser.semantic_error = True
            self.error.log_error(msg,2)

        if self.code == 1:
            msg = "No PRINCIPAL method was found"
            Parser.semantic_error = True
            self.error.log_error(msg,3)

        if self.code == 2:
            msg = "Only one PRINCIPAL method is allowed"
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if self.code == 3:
            msg = "PRINCIPAL does not receive any parameters"
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if self.code == 4:
            msg = "Semantic error found in line " + str(self.line) + "Data type assignation has been mismatched"
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if self.code == 5:
            msg = "Semantic error found in line " + str(self.line) + ". Undeclared variable was used or called"
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if self.code == 6:
            msg = "Semantic error found in line " + str(self.line) + "Arithmetic operators cannot be used with boolean data"
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if  self.code == 7:
            msg = "Runtime error found in line " + str(self.line) + ". Integer division by zero"
            Parser.semantic_error = True
            self.error.log_error(msg, 2)

        if self.code == 8:
            msg = "Semantic error found in line" + str(self.line) + ". Data type assignation has been mismatched "
            Parser.semantic_error = True
            self.error.log_error(msg, 3)

        if self.code == 9:
            msg = "Syntax error found in line " + str(self.line) + ". Declared time value is invalid"
            Parser.syntax_error = True
            print(Parser.syntax_error)
            self.error.log_error(msg, 2)

        if self.code == 10:
            msg = "Semantic error found in line " + str(self.line) + ". Keyword not recognized. Invalid keyword"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 11:
            msg = "Semantic error found in line " + str(self.line) + ". ---- cambiar error de este if ---- "
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 12:
            msg = "Semantic error found in line " + str(self.line) + ". Invalid movement"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 13:
            msg = "Semantic error found in line " + str(self.line) + ". Invalid time value"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 14:
            msg = "Semantic error found in line " + str(self.line) + ". Integers are not comparable with a boolean"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 15:
            msg = "Semantic error found in line " + str(self.line) + ". Declared variable was called"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 16:
            msg = "Semantic error found in line " + str(self.line) + ". FOR LOOP is out of range"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 17:
            msg = "Semantic error found in line " + str(self.line) + ". -- cambiar error --- MISSING BREAK EXPRESSION"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 18:
            msg = "Semantic error found in line " + str(self.line) + ". Variable is not valid"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 19:
            e_msg = "Semantic error found in line" + str(self.line) + ". -- cambiar error --- MAXIMUM RECURSION DEPTH EXCEEDED IN COMPARISON"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)

        if self.code == 20:
            msg = "Semantic error found in line" + str(self.line) + ". Parameters do not match"
            Parser.syntax_error = True
            self.error.log_error(msg, 3)