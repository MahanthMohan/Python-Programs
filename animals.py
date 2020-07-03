def animals(*args):
    animals = []
    for arg in args:
        animals.append(arg)
    legs = [2,4,4]
    res = 0
    for i in range(len(legs)): 
        ret = 1
        ret = animals[i] * legs[i]
        res = res + ret
    return res

print(animals(2,3,5))