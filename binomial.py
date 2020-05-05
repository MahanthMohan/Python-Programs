import math

class binomial:

    def factorial(self,n):
        self.n = n
        if(n == 1):
            return 1

        else:
            return n * binomial.factorial(n-1)

    def binomial(self,n,k):
        self.n = n
        self.k = k
        
        if(n == k):
            return 1

        else:
            coefficient = binomial.factorial(n)/(binomial.factorial(n - k) * binomial.factorial(k))
            return coefficient

binomial = binomial()

n = int(input("Enter the row: "))
k = int(input("Enter the term: "))
print(binomial.binomial(n,k), end = "")
