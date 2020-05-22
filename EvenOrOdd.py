class EvenOrOdd:

    def evenOrOdd(self,a,b):
        if a%b==0:
            print("The number {} is divisible by {}".format(a,b))
        else:
            print("The number {} is not divisible by {}".format(a,b))

EvenOrOdd = EvenOrOdd()

a = int(input("Enter the dividend: "))
b = int(input("Enter the divisor: "))
EvenOrOdd.evenOrOdd(a,b)
