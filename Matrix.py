import numpy as Math

def findInv():
    print(Math.linalg.inv(x))

def findDet():
    print(Math.linalg.det(x))

def findAdj():
    print(Math.linalg.adj(x))

row1 = input("Enter the values for row 1 of the matrix)
row2 = input("Enter the values for row 2 of the matrix)
row3 = input("Enter the values for row 3 of the matrix)
x = Math.array([row1],[row2],[row3])           
print ("This is the matrix that you created " + x) 
command = input("Enter the operation - Inverse, Determinant, or Adjugate")
if(command == 'Inverse')
   findInv() 
             
elif(command == 'Determinant')
   findDet() 

elif(command == 'Adjugate')
   findAdj()              
