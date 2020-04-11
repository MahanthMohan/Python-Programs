class calculator:

    def add(bruh,n1,n2):
        bruh.n1 = n1
        bruh.n2 = n2
        return bruh.n1 + bruh.n2

    def subtract(bruh,n1,n2):
        bruh.n1 = n1
        bruh.n2 = n2
        return bruh.n1 - bruh.n2

    def multiply(bruh,n1,n2):
        bruh.n1 = n1
        bruh.n2 = n2
        return bruh.n1 * bruh.n2

    def divide(bruh,n1,n2):
        bruh.n1 = n1
        bruh.n2 = n2
        return bruh.n1 / bruh.n2

calc = calculator()
print(calc.add(10,5) ,calc.subtract(10,5), calc.multiply(10,5), calc.divide(10,5))