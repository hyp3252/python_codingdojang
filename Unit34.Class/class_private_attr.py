# 비공개 속성 사용

# 클래스 바깥에서는 접근하지 못하고 클래스 안에서만 사용가능
# 앞에만 밑줄 두개


# Person 클래스에 wallet속성을 비공개로 해보면


# Person 클래스에 __wallet속성을 추가하고 돈이 모자라면 쓰지 못하는 식으로 만든다.    
class Person:
    def __init__(self, wallet):
        self.__wallet = wallet # 비공개 속성
        
    def pay(self, amount):
        print("기존금액 :", self.__wallet)
        print("결재금액 :" , amount)
        
        if self.__wallet < amount:
            print("잔액부족합니다. {}원을 더 충전해주세요.".format(amount-self.__wallet))
            return self.__wallet
        self.__wallet -= amount
        print("현재남은잔액 :", self.__wallet)
        
a = Person(10000)

a.pay(3000)
a.pay(4000)
a.pay(5000)


