import numpy as np

class monster:

    def eliminate(self,n,input):
        self.n = n
        self.input = input
        for i in range(0, self.n):
            if(i%2 != 0):
                output = [self.input[0][i]]
                return monster.eliminate(int(self.n/2),output)

monster = monster()
print(monster.eliminate(10,input = [(np.arange(1,101))]))

