import numpy as np

def function(n):
    a = 5
    r = 3
    if n == 1:
        return a
    else:
        return r * function(n-1)

def increment(i):
    if(i < 10):
     i += 1
    return function(i)
    
print (increment(1))
