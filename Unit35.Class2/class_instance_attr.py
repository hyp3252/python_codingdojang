# 클래스 속성과 인스턴스 속성


# 클래스속성 : 모든 인스턴스가 공유, 인스턴스 전체가 사용해야하는 값을 저장할 때 사용
# 인스턴스속성 : 인스턴스별로 독립되어 있다. 각 인스턴스가 값을 따로 저장해야 할 때 사용




# 클래스속성
class Person:
    bag = []
    
    def put_bag(self, stuff):
        self.bag.append(stuff)
a = Person()
a.put_bag("책")
A = a.bag
b = Person()
b.put_bag("화장품")
B = b.bag
print(A)
print(B)



# 인스턴스 속성 : 공유하지않으려면

class Person:
    def __init__(self):
        self.bag = []
        
    def put_bag(self, stuff):
        self.bag.append(stuff)
        
        
a = Person()
a.put_bag("책")

b = Person()
b.put_bag("화장품")

print(a.bag)
print(b.bag)



# 비공개 클래스 속성

class Knight:
    __item_limit = 10
    
    def print_item_limit(self):
        print(Knight.__item_limit)


x = Knight()
x.print_item_limit()


print(Knight.__item_limit) # 에러