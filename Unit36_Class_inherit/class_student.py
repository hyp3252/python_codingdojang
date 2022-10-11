# 기능을 물려주는 클래스를 기반클래스, 상속받아 새롭게 만드는 클래스를 파생 클래스


# 기반클래스(부모클래스, 슈퍼클래스), 파생 클래스(자식클래스, 서브 클래스)


class Person:
    def greeting(self):
        print("안녕")
        
        
        
class Student(Person): # Person 클래스의 기능을 물려받음.
    def study(self):
        print("공부하기")
        
        
James = Student()
James.greeting() # Student 클래스에는 없지만 Person 클래스를 상속을 받았기 때문에 호출 가능
James.study()




