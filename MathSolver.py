import requests

class MathSolver:
    
    def intro(self):
        common_operations = "operations: simplify, factor, derive, integrate, zeroes, tangent, area, cosin, sin, tan, arcos, arcsin, arctan, abs, log"
        expression = "All entered expressions should be algebraic"
        return "\n" + common_operations + "\n" + expression

    def calculate(self, operation, expression):
        self.operation = operation
        self.expression = expression
        API_URL = "https://newton.now.sh/operation/expression"
        request_URL = "https://newton.now.sh/{}/{}".format(operation,expression)
        return_data = requests.get(request_URL).json()
        result = return_data['result']
        return result

solve = MathSolver()
