import numpy as Math

def findInv():
    print(Math.linalg.inv(A))

def findDet():
    print(Math.linalg.det(A))

def findAdj():
    A_Prime = A

a = input()
b = input()
c = input()
d = input()

A = Math.array([[a],[b],[c],[d]])
         
print (A)

command = input("Enter the operation - Inverse, Determinant, or Adjugate ")
if(command == 'Inverse'):
   findInv() 
             
elif(command == 'Determinant'):
   findDet() 

elif(command == 'Adjugate'):
   findAdj()    