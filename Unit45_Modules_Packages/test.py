# from calcpkg.calc_geometry import *
# from calcpkg.calc_operation import *

# num = int(input())

# print(squareroot(num))
# print(circle_area(num))



import calcpkg.calc_geometry
import calcpkg.calc_operation

num = int(input())
print(calcpkg.calc_operation.squareroot(num))
print(calcpkg.calc_geometry.circle_area(num))