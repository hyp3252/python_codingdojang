# 클래스로 점 구현



class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
        
p1 = Point2D(30, 20)
p2 = Point2D(60, 50)


print("p1 : {} {}".format(p1.x, p1.y))
print("p2 : {} {}".format(p2.x, p2.y))


## 피타고라스 정리로 두 점 거리 구하기
## 대입하려면 밑변 a, 높이 b를 구한다.
## 루트는 math.sqrt 사용
import math
a = p1.x - p2.x
b = p1.y - p2.y
c = math.sqrt(a**2 + b**2)
print(c)



## 제곱은 pow 함수를 사용해도 된다.

c = math.sqrt(math.pow(a,2) + math.pow(b,2)) # a^2 , b^2
print(c)