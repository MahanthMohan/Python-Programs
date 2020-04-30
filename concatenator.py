def concatenate(a,b):
    if (type(a) and type(b) == "<class 'int'>"):
        res = str(a) + str(b)
        return res

    else:
        res = int(a) + int(b)
        return res

print(concatenate(int(12),int(13)))