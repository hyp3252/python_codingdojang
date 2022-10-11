# 클래스란?
# 클래스는 객체를 표현하기 위한 문법
# 게임을 만든다고 하면, 직업별 클래스 캐릭터들,등등
# 프로그래밍으로 객체를 만들 때 사용하는 것이 클래스

class 클래스이름:
    def method(self):
        print('hello')
        
        
        


class Person:
    def greeting(self):
        print("hello")
        
        
        
        
James = Person() # James는 Person의 인스턴스

James.greeting() # 인스턴스 method

Person().greeting()