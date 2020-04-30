import math

class square:
    def collectradius(self):
        radius = float(input("Enter the radius of the circle: "))
        return radius

    def square(self,radius):
        self.radius = radius
        diameter = float(2 * radius)
        side = diameter / 2**0.5
        result = "The area of the inscribed square is " + str(round(side * side, 2))
        return result

square = square()

print(square.square(square.collectradius()))

