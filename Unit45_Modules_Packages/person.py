# person module
# 모듈에 클래스 작성하기

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
        
        
    def greeting(self):
        print("안녕하세요 저는 {}이고, 나이는 {}이고, 사는곳은 {}입니다."\
            .format(self.name, self.age, self.address))