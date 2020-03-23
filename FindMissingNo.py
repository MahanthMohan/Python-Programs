import numpy as np

original_matrix = np.matrix([1,2,3,4,5,6,7,8,9,10]).reshape(1,10)
R = int(input("Enter the number of rows: ")) 
C = int(input("Enter the number of columns: ")) 
print("Enter the entries in a single line, rowwise , and spaced out using commas ") 
enter_values = list(map(int, input().split(","))) 
M = np.matrix(enter_values).reshape(R, C) 
