
class factorial:

    def factorial(self,n):
        self.n = n
        if(n == 1):
            return 1
        else:
            return n * fact.factorial(n - 1)

fact = factorial()
print(fact.factorial(4))