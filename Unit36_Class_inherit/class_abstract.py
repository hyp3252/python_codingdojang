# 추상클래스

# 메서드의 목록만 가진 클래스이며 상속받는 클래스에서 메서드 구현을 강제하기 위함

# 인스턴스로 만들 때는 사용하지 않으며 오로지 상속에만 이용
# 파생클래스에서 반드시 구현해야 할 메소드를 정해 줄 때 사용

from abc import *

class StudentBase(metaclass=ABCMeta):
    @abstractmethod
    def study(self):
        pass
    
    @abstractmethod
    def go_to_school(self):
        pass
    

class Student(StudentBase):
    def study(self): # 상속을 받았어도 구현을 해야한다.
        print("공부하기")
        
        
    # def go_to_school(self): # 상속을 받았어도 구현을 해야한다.
    #     print("학교가기")
        
        
        
james = Student() # 하나라도 구현하지않으면 에러발생
# james.study()
# james.go_to_school()
