import numpy as Math # To import numpy package as "Math" for linalg operations with Matrices 

def BasicOps(): # Basic Operations such as add, subtarct, multiply, and divide
    bcommand = input("Enter an operation - add, subtract, multiply, and divide ") # Takes user input for the command
    if(bcommand == "add"): # add
     X = Math.matrix(enter_values).reshape(R, C)
     M = Math.linalg.solve(M + X)
     print(M)
    
    elif(bcommand == "subtract"): # subtract
     X = Math.matrix(enter_values).reshape(R, C)
     M = Math.linalg.solve(M - X)
     print(M)   
    
    elif(bcommand == "multiply"): # multiply
     X = Math.matrix(enter_values).reshape(R, C)
     M = Math.linalg.solve(M * X)
     print(M)  
     
    elif(bcommand == "divide"):  # divide
     X = Math.matrix(enter_values).reshape(R, C)
     M = Math.linalg.solve(M / X)
     print(M) 
      
def LinearAlg():
    bcommand = input("Enter an operation - Inverse or Determinant ") # Takes user input for the command
    if(bcommand == "Inverse"): # Inverse
     M = Math.linalg.inv(M)
     print(M)
     
    elif(bcommand == "Determinant"): # Determinant
     M = Math.linalg.det(M)
     print(M)
              
# User input for rows and columns  
R = int(input("Enter the number of rows: ")) 
C = int(input("Enter the number of columns: ")) 
  
  
print("Enter the entries in a single line, rowwise , and spaced out using commas ") 
   
# single line separated by space 
enter_values = list(map(float, input().split(","))) # Logic - seperates the float values by taking ',' as a reference, and the map operator accepts values until all rows and columns are maxed out
  
# For printing the matrix 
M = Math.matrix(enter_values).reshape(R, C)  # "Reshapes" it into a matrix
print("This is your original Matrix")
print(M)

command = input("Do you wish to do basicops, complexops, or exit? ") # Continue or exit dialog
if(command == "exit"):
    input.close()
    
elif(command == "basicops"):
    BasicOps()    
    
elif(command == "complexops"):
    LinearAlg()




 
    