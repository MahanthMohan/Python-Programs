import numpy as np

class monster:

    def eliminate(self,n,input):
        self.n = n
        self.input = input
        for i in range(0,n):
            if(i%2 != 0):
                output = [input[0][i]]
                test = output
                return monster.eliminate(n,test)

monster = monster()
print(monster.eliminate(10,input = [(np.arange(1,101))]))

