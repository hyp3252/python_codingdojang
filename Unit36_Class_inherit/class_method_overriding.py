# 메서드 오버라이딩
# 기반 클래스의 메서드를 무시하고 새로운 메서드를 만든다

# Person 클래스의 greeting메소드를 무시하고 Student클래스에서 새로운 greeting 메소드를 만든다.

# 보통 프로그램에서 어떤 기능이 같은 이름의 메소드로 계속 사용되어야 할 때 메소드 오버라이딩을 활용
# 중복되는 기능은 파생 클래스에서 다시 만들지 않고 기반 클래스의 기능을 사용
# 메소드 오버라이딩은 원래 기능을 유지하면서 새로운 기능을 덧붙일 때 사용


class Person:
    def greeting(self):
        print("안녕하세요")
        
        
class Student(Person):
    def greeting(self):
        super().greeting() # 기반 클래스의 메서드를 호출하여 중복을 줄인다.
        print("안녕하세요 코딩도장 독학생입니다.")
        
        
        
james = Student()
james.greeting()