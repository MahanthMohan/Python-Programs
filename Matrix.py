import numpy as Math # To import numpy package as "Math" for linalg operations with Matrices 
import sys

# Methods start 
             
# User input for rows and columns
def MatrixInputM():  
 R = int(input("Enter the number of rows: ")) 
 C = int(input("Enter the number of columns: ")) 
 print("Enter the entries in a single line, rowwise , and spaced out using commas ") 
 # single line separated by space 
 enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
 # For printing the matrix 
 M = Math.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
 print("This is your original Matrix")
 print(M)
 return M
 
def MatrixInputX():
  print("Enter the values for the second matrix")  
  R = int(input("Enter the number of rows: ")) 
  C = int(input("Enter the number of columns: ")) 
  print("Enter the entries in a single line, rowwise , and spaced out using commas ") 
  # single line separated by space 
  enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
  # For printing the matrix 
  X = Math.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
  print("This is the second matrix")
  print(X)
  return X

def BasicOps(): # Basic Operations such as add, subtarct, multiply, and divide
    bcommand = input("Enter an operation - add, subtract, multiply, and divide ") # Takes user input for the command
    M = MatrixInputM()
    X = MatrixInputX()
    if(bcommand == "add"): # add
     result = Math.linalg.solve(M + X)
     print(result)
    
    elif(bcommand == "subtract"): # subtract
     result = Math.linalg.solve(M - X)
     print(result)   
    
    elif(bcommand == "multiply"): # multiply
     result = Math.linalg.solve(M * X)
     print(result)  
     
    elif(bcommand == "divide"):  # divide
     result = Math.linalg.solve(M / X) 
     print(result) 
      
def LinearAlg():
    bcommand = input("Enter an operation - Inverse or Determinant ") # Takes user input for the command
    M = MatrixInputM()
    X = MatrixInputX()
    if(bcommand == "Inverse"): # Inverse
     MatrixInputM()    
     result = Math.linalg.inv(M)
     print(M)
     
    elif(bcommand == "Determinant"): # Determinant
     MatrixInputM()   
     result = Math.linalg.det(M)
     print(M)

# Methods end

command = input("Do you wish to do basicops, complexops, or exit? ") # Actual Program (Main) starts from here
if(command == "exit"):
    sys.exit()
    
elif(command == "basicops"):
    BasicOps()    
    
elif(command == "complexops"):
    LinearAlg() 
    



 
    