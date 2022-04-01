class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class TambInstructions(metaclass=SingletonMeta):
    def __init__(self):
        self.log = []

    def log_tamb(self, msg):
        self.log.append(msg)

    def print(self):
        print(self.log)

    def value(self):
        return self.log

    def clean(self):
        self.log = []