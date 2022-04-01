class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class print_log(metaclass=SingletonMeta):
    def __init__(self):
        self.log = ""

    def log_print(self, msg):
        self.log += msg + "\n"
        print("SE AGREGO UN NUEVO PRINT --> " + self.log)

    def print(self):
        print(self.log)

    def value(self):
        return self.log

    def clean(self):
        self.log = ""