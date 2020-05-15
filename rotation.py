import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math

class rotation:
    def input(self):
        angle = float(input("Angle measure: "))
        coordinates = input("Vector coordinates: ")
        splitted_coordinates = coordinates.split(",")
        input_values = [float(element) for element in splitted_coordinates]
        vector = np.matrix([input_values]).reshape(3,1)
        return_list = [angle,vector]
        return return_list

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

    def tr_vector(self, vector, transform_matrix):
        self.transform_matrix = transform_matrix
        self.vector = vector
        tr_vector = np.dot(transform_matrix,vector)
        return tr_vector

rotate = rotation()

list = rotate.input()

print(rotate.tr_vector(list[1],rotate.transform(list[0])))

"""   
fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
X,Y,Z = list[1]
ax.plot(X,Y,Z)
plt.show()
"""





