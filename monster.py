import numpy as np

class monster:

    def eliminate(self,n):
        self.n = n
        for i in range(0, self.n - 1):
            if(i%2 != 0):
                initial_values = np.array([np.arange(1,self.n)])
                out = np.matrix([initial_values[0][i]]).reshape(1,int(self.n/2))

monster = monster()
monster.eliminate(1000)      


