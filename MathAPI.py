import requests
operation = input("Enter any operation ")
expression = input("Enter the expression ")
API_URL = "https://newton.now.sh/operation/expression"
request_URL = "https://newton.now.sh/" + operation + "/" + expression
return_data = requests.get(request_URL).json()
result = return_data['result']
print(result)