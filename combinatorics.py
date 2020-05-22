import math as m

class combinatorics:

    # Order does not matter
    def Combination(self,n,r):
        self.n = n
        self.r = r
        result = m.factorial(n)/(m.factorial(n-r)*m.factorial(r))
        return result

    # Order matters
    def Permutation(self,n,r):
        self.n = n
        self.r = r
        result = m.factorial(n)/m.factorial(n-r)
        return result

combinatorics = combinatorics()

n = int(input("Enter the total number: "))
r = int(input("Enter number selected: "))
print(combinatorics.Combination(n,r))
print(combinatorics.Permutation(n,r))
