class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, stack):
        super().__init__(name)
        self.stack = stack

dev = Developer("Alim", ["Python", "FastAPI"])
print(dev.name, dev.stack)
