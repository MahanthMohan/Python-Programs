import numpy as np

print("*** A solver for the systems of equations Ax + By = C ***")

R = int(input("Enter the number of rows: ")) 
C = int(input("Enter the number of columns: "))
 
print("Enter the entries in a single line for the A matrix, rowwise , and spaced out using commas ") 
# single line separated by space 
enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
# For printing the matrix 
A = np.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
print("\nThis is the A Matrix")
print(A)

print("Enter the entries in a single line for the B matrix, rowwise , and spaced out using commas ") 
# single line separated by space 
enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
# For printing the matrix 
C = np.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
print("\nThis is the C Matrix")
print(C)

B = np.linalg.solve(A,C)
print("\nThis is the vector solution to the systems of equations")
print(B)



