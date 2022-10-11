# 표준 입력으로 x, y 좌표 4개가 입력되어 Point2D 클래스의 인스턴스 리스트에 저장됩니다.
# 여기서 점 4개는 첫 번째 점부터 마지막 점까지 순서대로 이어져 있습니다.
# 다음 소스 코드를 완성하여 첫 번째 점부터 마지막 점까지 연결된 선의 길이가 출력되게 만드세요.


import math

from cv2 import line
 
class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
 
length = 0.0
p = [Point2D(), Point2D(), Point2D(), Point2D()]
p[0].x, p[0].y, p[1].x, p[1].y, p[2].x, p[2].y, p[3].x, p[3].y = map(int, input().split())

for i in range(3):
     line = math.sqrt(pow(p[i].x-p[i+1].x , 2) + pow(p[i].y-p[i+1].y , 2))
     length += line
     

# first_line = math.sqrt(pow(p[0].x-p[1].x , 2) + pow(p[0].y-p[1].y , 2))
# second_line = math.sqrt(pow(p[1].x-p[2].x , 2) + pow(p[1].y-p[2].y , 2))
# third_line = math.sqrt(pow(p[2].x-p[3].x , 2) + pow(p[2].y-p[3].y , 2))
# length = first_line + second_line + third_line


print(length)