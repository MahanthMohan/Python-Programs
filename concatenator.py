def concatenate(a,b):
    if (type(a) and type(b) == "integer"):
        res = str(a) + str(b)
        return res

    else:
        res = int(a) + int(b)
        return res

print(concatenate(12,13))