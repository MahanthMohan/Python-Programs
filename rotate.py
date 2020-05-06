import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import math

class rotate:

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

    def transformvector(self):
        enter_values = input("Enter the vector coordinates: ")
        splitted_values = enter_values.split(",")
        vector = np.matrix([splitted_values]).reshape(1,3)
        print(vector)


rotate = rotate()

fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
X,Y,Z = np.array([1],[1],[1])
ax.plot_wireframe(X,Y,Z)
plt.show()
angle = float(input("Enter an angle measure: "))
print(rotate.transform3d(angle))