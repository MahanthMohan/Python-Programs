import numpy as np

class monster:

    def eliminate(self,n):
        self.n = n
        for i in range(0, self.n):
            if(n == 0):
                return 0
            elif(n > 0 and i%2 != 0):
                initial_values = np.array([np.arange(1,self.n + 1)])
                output = np.array([initial_values[0][i]])

monster = monster()
print()

