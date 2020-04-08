import requests
common_operations = "operations: simplify, factor, derive, integrate, zeroes, tangent, area, cosin, sin, tan, arcos, arcsin, arctan, abs, log"
expression = "All entered expressions should be algebraic"
print("\n" + common_operations + "\n" + expression)
operation = input("Enter any operation: ")
expression = input("Enter the expression: ")
API_URL = "https://newton.now.sh/operation/expression"
request_URL = "https://newton.now.sh/" + operation + "/" + expression
return_data = requests.get(request_URL).json()
result = return_data['result']
print(result)
