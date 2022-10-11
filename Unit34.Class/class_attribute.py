# 클래스에서 속성을 만들고 사용해본다.



from unicodedata import name


class Person:
    def __init__(self):
        self.hello = "안녕하세요"
        
    def greeting(self):
        print(self.hello)
        
James = Person()

James.greeting()

# 앞뒤로 _ 두개가 붙은 method는 파이썬이 자동으로 호출해주는 메소드인데 스페셜 메소드 또는 매직 메소드라고 부른다.
# self는 인스턴스 자기 자신을 의미

# 인스턴스 만들 때 값 받기
class Person:
    def __init__(self, name, age, address):
        self.hello = "안녕하세요"
        self.name = name
        self.age = age
        self.address = address
        
    def greeting(self):
        print("{}저는 {} 입니다. 나이는 {}살이구요. 사는 곳은 {} 입니다.".format(self.hello, self.name, self.age, self.address))

maria = Person("마리아", 26, "대전시 유성구 도안동")
maria.greeting()


print(maria.hello)
print(maria.name)
print(maria.age)
print(maria.address)


