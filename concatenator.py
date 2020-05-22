class concatenator:

    def concatenate(self,a,b):
        self.a = a
        self.b = b
        if (type(a) and type(b) == "<class 'int'>"):
            res = str(a) + str(b)
            return res

        else:
            res = int(a) + int(b)
            return res

concatenator = concatenator()

print(concatenator.concatenate(int(12),int(13)))