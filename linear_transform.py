import numpy as np
import math

class linalg:

    def CollectAngleInput(self):
        transform_angle = float(input("Rotation angle: "))
        return transform_angle

    def transform2d(self,transform_angle):
        self.transform_angle = transform_angle
        rad_angle = (transform_angle * (math.pi/180))
        input_values =  math.cos(rad_angle),(-1) * math.sin(rad_angle),math.sin(rad_angle),math.cos(rad_angle)
        rounded_values = [round(element, 3) for element in input_values]
        transform_matrix = np.matrix(rounded_values).reshape(2,2)
        return transform_matrix
    
    def transform3d(self,transform_angle):
        self.transform_angle = transform_angle
        local_command = input("Enter a type of rotation (X,Y, or Z): ")
        if local_command == "X":
            rad_angle = (transform_angle * (math.pi/180))
            input_values =  1,0,0,0,math.cos(rad_angle),(-1)*math.sin(rad_angle),0,math.sin(rad_angle),math.cos(rad_angle)
            rounded_values = [round(element, 3) for element in input_values]
            transform_matrix = np.matrix(rounded_values).reshape(3,3)
            return transform_matrix

        elif local_command == "Y":
            rad_angle = (transform_angle * (math.pi/180))
            input_values =  math.cos(rad_angle),0,math.sin(rad_angle),0,1,0,(-1)*math.sin(rad_angle),0,math.cos(rad_angle)
            rounded_values = [round(element, 3) for element in input_values]
            transform_matrix = np.matrix(rounded_values).reshape(3,3)
            return transform_matrix
            
        elif local_command == "Z":
            rad_angle = (transform_angle * (math.pi/180))
            input_values =  math.cos(rad_angle),(-1)*math.sin(rad_angle),0,math.sin(rad_angle),math.cos(rad_angle),0,0,0,1
            rounded_values = [round(element, 3) for element in input_values]
            transform_matrix = np.matrix(rounded_values).reshape(3,3)
            return transform_matrix


lin = linalg()

command = input("Enter a command (2D or 3D): ")
if (command == '2D'):
    print(lin.transform2d(lin.CollectAngleInput()))
elif (command == '3D'):
    print(lin.transform3d(lin.CollectAngleInput()))
