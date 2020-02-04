def getInput():
    lower_limit = int(input("Enter the lower value: "))
    upper_limit = int(input("Enter the upper value: "))
    array = [lower_limit,upper_limit]
    print(array)
    return array

def doThing(a,b):
    print (a,b)

array = getInput()
doThing(array[0],array[1])


