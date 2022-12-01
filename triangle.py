from cmath import sqrt

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
    
    def gety(self):
        return self.__y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__puntos = [vertice1.getx(), vertice1.gety(), vertice2.getx(), vertice2.gety(), vertice3.getx(), vertice3.gety()]

    def perimeter(self):
        self.__per = sqrt((self.__puntos[0] - self.__puntos[2])**2 + (self.__puntos[1] - self.__puntos[3])**2) + sqrt((self.__puntos[2] - self.__puntos[4])**2 + (self.__puntos[3] - self.__puntos[5])**2) + sqrt((self.__puntos[4] - self.__puntos[0])**2 + (self.__puntos[5] - self.__puntos[1])**2)
        return self.__per

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())

# Compare this snippet from triangle.py:
# import math


# class Point:
#     def __init__(self, x=0.0, y=0.0):
#         self.__x = x
#         self.__y = y

#     def getx(self):
#         return self.__x

#     def gety(self):
#         return self.__y

#     def distance_from_xy(self, x, y):
#         return math.hypot(abs(self.__x - x), abs(self.__y - y))

#     def distance_from_point(self, point):
#         return self.distance_from_xy(point.getx(), point.gety())


# class Triangle:
#     def __init__(self, vertice1, vertice2, vertice3):
#         self.__vertices = [vertice1, vertice2, vertice3]

#     def perimeter(self):
#         per = 0
#         for i in range(3):
#             per += self.__vertices[i].distance_from_point(self.__vertices[(i + 1) % 3])
#         return per


# triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
# print(triangle.perimeter())
