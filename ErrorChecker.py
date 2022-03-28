class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class ErrorChecker(metaclass=SingletonMeta):
    def __init__(self):
        self.log_lex = ""
        self.log_syn = ""
        self.log_sem = ""

    def log_error(self, msg, log):
        if log == 1:
            print("Se ha agregado un error léxico--> " + msg)
            self.log_lex += msg + "\n"
        elif log == 2:
            print("Se ha agregado un error sintactico--> " + msg)
            self.log_syn += msg + "\n"
        else:
            print("Se ha agregado un error semántico--> " + msg)
            self.log_sem += msg + "\n"


    def print(self):
        print(self.log_lex, self.log_syn, self.log_sem)

    def errors(self):
        if self.log_lex != "":
            return self.log_lex
        elif self.log_syn != "":
            return self.log_syn
        else:
            return self.log_sem

    def clean(self):
        self.log_lex = ""
        self.log_syn = ""
        self.log_sem = ""