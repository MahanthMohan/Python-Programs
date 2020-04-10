
class Calculator:

    def __init__(self,n1 = 10,n2 = 5):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return self.n1 + self.n2

    def subtract(self):
        return self.n1 - self.n2

    def multiply(self):
        return self.n1 * self.n2

    def divide(self):
        return self.n1 / self.n2

calc = Calculator()

print(calc.add())
print(calc.subtract())
print(calc.multiply())
print(calc.divide())
