import math as m

# Order does not matter
def Combination(n,r):
    result = m.factorial(n)/(m.factorial(n-r)!*m.factorial(r))
    return result

# Order matters
def Permutation(n,r):
    result = m.factorial(n)/m.factorial(n-r)
    return result

print(Combintion(n,r))
print(Permutation(n,r))