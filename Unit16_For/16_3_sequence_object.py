# list에 있는 값들을 순서대로가져오기

print("List에 있는 값들을 순서대로 가져오기")
a = [10,20,30,40,50]

for i in a:
    print(i)

# 튜플에 있는 값들을 가져오기
print("튜플에 있는 값들을 순서대로 가져오기")
fruits = ['apple', 'banana', 'pineapple', 'melon', 'watermelon']
for fruit in fruits:
    print(fruit)

# 문자열도 시퀀스 객체이므로 for에 문자열을 지정하면 문자도 반복
print("문자열에서 하나씩 꺼내면서 반복")
for letter in reversed('Python'):
    print(letter, end='.')