import numpy as Math # To import numpy package as "Math" for linalg operations with Matrices 
import sys # A package 
# Methods start 
    
def LinearAlg():
    command = input("Enter an operation - Inverse, Determinant, Exponent, or Adjugate: ") # Takes user input for the command
    if(command == "Inverse"): # Inverse  
        result = Math.linalg.inv(M)
        print("This is the Inverse Matrix")
        print(result)
     
    elif(command == "Determinant"): # Determinant
        result = Math.linalg.det(M)
        print("This is the Determinant of the Matrix")
        print(result)
    
    elif(command == "Exponent"): # Exponent
        n = int(input("Enter the power the matrix needs to be raised to: "))
        result = Math.linalg.matrix_power(M,n)
        
    elif(command == "Adjugate"): # Adjugate
        print("These are the values for the adjugate matrix")
        res_matrix = [[i for i in range(R)] for j in range(C)] # Specifies the range to the number of rows and columns
        for i in range(R): # Conditional for loop to calculate adjugate
          for j in range(C):
             res_matrix[i][j] = (-1)*(i+j)*(Math.linalg.det(M)) # logic - -1 * (matrix det * switched row and column)
             print(res_matrix[i][j]) # prints values of the adjugate matrix in [1*x] form
        
        
# Methods end here

command = input("Do you wish to continue or exit? ") # Actual Program (Main) starts from here
if(command == "exit"):
    print("Thank you for your time")
    sys.exit()
       
elif(command == "continue"):
    R = int(input("Enter the number of rows: ")) 
    C = int(input("Enter the number of columns: ")) 
    print("Enter the entries in a single line, rowwise , and spaced out using commas ") 
    # single line separated by space 
    enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
    # For printing the matrix 
    M = Math.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
    print("This is your original Matrix")
    print(M)
    LinearAlg() # Calls the linear algebra method defined above