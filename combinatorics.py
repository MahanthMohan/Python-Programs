import math as m

# Order does not matter
def Combination(n,r):
    result = m.factorial(n)/(m.factorial(n-r)*m.factorial(r))
    return result

# Order matters
def Permutation(n,r):
    result = m.factorial(n)/m.factorial(n-r)
    return result

n = int(input("Enter the total number: "))
r = int(input("Enter number selected: "))
print(Combination(n,r))
print(Permutation(n,r))
