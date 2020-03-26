import numpy as np

def Missing_no():
    n_sum = (n * (n+1))/2
    print("The missing number is: ")
    print(n_sum - mat_sum)

print("*** A program to find the missing number in a list ***")    
n = int(input("Number of values to be entered: "))
print("Enter the values: ")
enter_values = list(map(float, input().split(",")))
A = np.matrix(enter_values).reshape(1, n - 1)
print("These are the entered values")
mat_sum = A.sum()
print(mat_sum)
Missing_no()

