# 포함관계


class Person:
    def greeting(self):
        print("안녕하세요")
        
class PersonList():
    def __init__(self):
        self.person_list = []
        
    def append_person(self, person):
        self.person_list.append(person)
        
        
# 기반 클래스의 속성 사용
# super() 로 기반클래스 초기화
# super()를 사용하여 기반 클래스의 __init__ 메서드를 호출
class Person:
    def __init__(self):
        print('Person __init__')
        self.hello = "안녕하세요"
        
class Student(Person):
    def __init__(self):
        print("Student __init__")
        super().__init__()
        self.school = "파이썬 코딩도장 독학"
        
James = Student()
print(James.hello)
print(James.school)