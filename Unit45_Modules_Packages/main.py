# 모듈을 만들고 그 모듈에서 import하는 방법

# ## 1번째 방법
# import square2

# print(square2.num) # 모듈.변수 형식으로 모듈의 변수출력 
# print(square2.square(10)) # 모듈.함수()형식으로 모듈의 함수 사용


# ## 2번째 방법


# from square2 import num, square

# print(num)
# print(square(10))


# import person

# m = person.Person("마리아", 24, "대전시 유성구")
# m.greeting()


# import module_startpoint
# print("main.py __name__", __name__)


# import calculator

# print(calculator.add(10,20))

# print(calculator.mul(30,50))



import calcpkg.calc_operation
import calcpkg.calc_geometry

print(calcpkg.calc_operation.add(10,20))
print(calcpkg.calc_operation.mul(10,20))

print(calcpkg.calc_geometry.triangle_area(20,10))
print(calcpkg.calc_geometry.rectangle_area(20,10))