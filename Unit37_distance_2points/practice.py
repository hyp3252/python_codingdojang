# 사각형 넓이 구하기

# 다음 소스 코드를 완성하여 사각형의 넓이가 출력되게 만드세요.


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
    def cal_area(self):
        width = abs(self.x1 - self.x2)
        height = abs(self.y1 - self.y2)
        area = width * height
        print(area)
    

rect = Rectangle(20,20,40,30)
rect.cal_area()