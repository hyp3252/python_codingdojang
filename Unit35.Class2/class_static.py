
# 정적 메소드는 @staticmethod
# 매개변수에 self를 사용하지 않는다.


class Calc:
    @staticmethod
    def add(a,b):
        print(a+b)
        
    @staticmethod
    def mul(a,b):
        print(a*b)
        

Calc.add(10,20) # 클래스에서 메소드 바로 호출
Calc.mul(10,20) # 클래스에서 메소드 바로 호출

# 정적메소드는 self를 받지않으므로 인스턴스 속성에 접근불가
# 정적메소드는 외부 상태에 영향을 끼치지않는 순수 함수를 만들 때 사용
# 