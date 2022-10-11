# 난수생성

import random
print(random.random())
i=0
while i!=3:
    i = random.randint(1,6)
    print(i)

# random.choice
# 시퀀스 객체에서 요소를 무작위로 선택가능, list, tuple, range, 문자열 등에서 사용가능

dice = [1,2,3,4,5,6]
print(random.choice(dice))