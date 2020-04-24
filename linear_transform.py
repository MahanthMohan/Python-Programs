import numpy as np
import math

class linalg:
    def CreateMatrix(self,R,C):
        self.R = R
        self.C = C
        input_values = input("Enter the coordinates of the vector: ")
        M = np.matrix(input_values).reshape(R,C)
        return M

    def CollectAngleInput(self):
        transform_angle = float(input("Enter an angle measure: "))
        return transform_angle

    def transform2d(self,vector,transform_angle):
        self.transform_angle = transform_angle
        self.vector = vector
        input_values =  math.cos(transform_angle),(-1) * math.sin(transform_angle),math.sin(transform_angle),math.cos(transform_angle)
        transform_matrix = np.matrix(input_values).reshape(2,2)
        transformed_vector = np.dot(vector,transform_matrix)
        return transformed_vector
        
        

lin = linalg()

vector = lin.CreateMatrix(R = int(input("Enter the number of rows (r<=2): ")), C = 2)
print(lin.transform2d(vector,lin.CollectAngleInput()))
