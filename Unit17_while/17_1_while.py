# while반복문은 조건식으로만 동작하며, 반복할 코드 안의 조건식에 영향을 주는 변화식이 들어간다
#
i = 0
while i < 100:
    print(i+1, "hello world")
    i += 1

# 초기값을 1로시작
i=1
while i <= 100:
    print(i , "Hello, world")
    i += 1


# 초기값을 감소
i = 100
while i > 0:
    print(i , "Hello world")
    i -= 1
# 입력한 횟수대로 반복
count = int(input('반복할 횟수 입력 : '))
i = 0
while i<count:
    print(i,"Hello world")
    i += 1

#