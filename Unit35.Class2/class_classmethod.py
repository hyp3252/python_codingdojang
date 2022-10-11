
# 클래스 메소드는 @classmethod를 붙인다.
# 첫번째 매개변수에 cls를 지정을해야한다.

from regex import P


class Person:
    count = 0
    
    def __init__(self):
        Person.count += 1 # 인스턴스가 만들어질때 1씩 늘어남
        
    
    
    @classmethod
    def print_count(cls):
        print("{0} 명이 생성되었습니다.".format(cls.count)) # cls로 클래스 속성에 접근
        
    @classmethod
    def create(cls):
        p = cls()
        return P
        
        
james = Person()
maria = Person()
Person.create()


Person.print_count()
