
# 다중상속 : 여러 기반 클래스로부터 상속을 받아 파생클래스를 만드는방법



# 사람클래스와 대학교 클래스를 만든 뒤 다중 상속으로 대학생 클래스를 만든다


# class Person:
#     def greeting(self):
#         print("안녕하세요")
        
        
# class University:
#     def manage_credit(self):
#         print("학점관리")
        

# class Undergraduate(Person, University):
#     def study(self):
#         print("공부하기")
        
        
        
        
# A = Undergraduate()
# A.greeting()
# A.manage_credit()
# A.study()



# 다이아몬드 상속


class A:
    def greeting(self):
        print("안녕하세요 A class입니다")
        
class B(A):
    def greeting(self):
        print("안녕하세요 B class 입니다")
        
    def a(self):
        print("아무거나")
        
class C(A):
    def greeting(self):
        print("안녕하세요 C class 입니다")
        
class D(B,C):
    pass


print(D.mro())
x = D()
x.greeting()

# Method Resolution Order, MRO를 통해 메소드 탐색순서가 나온다.
