import requests

food = input("Enter the food to find the no of calories: ")
quantity = input("Enter the quantity: ")
API_URL = "https://api.edamam.com/api/nutrition-data?app_id=c9cbde61&app_key=f60cf02c468169987d92a0f2acd160a2&ingr="
request_URL =  "https://api.edamam.com/api/nutrition-data?app_id=c9cbde61&app_key=f60cf02c468169987d92a0f2acd160a2&ingr={}%20{}".format(quantity,food)
return_data = requests.get(request_URL).json()

if(int(quantity) == 1):
    calories = '{} {} contains '.format(quantity,food) + str(int(return_data['calories'])) + ' calories'
    print(calories)


elif(int(quantity) > 1):
    calories = '{} {}s contains '.format(quantity,food) + str(int(return_data['calories'])) + ' calories'
    print(calories)
