def evenOrOdd(a,b):
    if a%b==0:
        print("The number {} is divisible by {}".format(a,b))
    else:
        print("The number {} is not divisible by {}".format(a,b))    


a = int(input("Enter the dividend "))
b = int(input("Enter the divisor "))
evenOrOdd(a,b)