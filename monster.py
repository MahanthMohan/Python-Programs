import numpy as np

class monster:

    def eliminate(self,n):
        self.n = n
        for i in range(0, self.n):
            if(i%2 == 0):
                i = i
                initial_values = np.array([np.arange(1,n)])
                rem = initial_values[0][i]
                print(rem)

monster = monster()
monster.eliminate(1000)      


