import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math

class rotation_animation:

    def transform(self,transform_angle):
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

    def transformvector(self, transform_matrix):
        self.transform_matrix = transform_matrix
        enter_values = input("Enter the vector coordinates: ")
        splitted_values = enter_values.split(",")
        input_values = [int(element) for element in splitted_values]
        vector = np.matrix([input_values]).reshape(1,3)
        transform_vector = np.dot(transform_matrix,vector)
        return transform_vector

rotate = rotation_animation()

"""     
fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
X,Y,Z = 1,2,3
ax.plot_wireframe(X,Y,Z)
plt.show()
"""
angle = float(input("Enter an angle measure: "))
print(rotate.transformvector(rotate.transform(angle)))

