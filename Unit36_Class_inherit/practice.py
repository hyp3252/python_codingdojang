# 다음 소스 코드에서 리스트(list)에 replace 메서드를 추가한 AdvancedList 클래스를 작성하세요. 
# AdvancedList는 list를 상속받아서 만들고, replace 메서드는 리스트에서 특정 값으로 된 요소를 찾아서 다른 값으로 바꾸도록 만드세요.




class AdvancedList(list):
    def replace(self, old, new):
        while old in self:
            self[self.index(old)] = new
        



x = AdvancedList([1, 2, 3, 1, 2, 3, 1, 2, 3])
x.replace(1, 100)
print(x)

# list를 상속받아서 AdvancedList를 만든다.

# 메소드안에서 현재 객체를 조작하려면 self를 이용한다. AdvancedList가 list를 상속받았으므로 self로 리스트의 모든 메소드를 사용할 수 있다.
# 특정값을 찾을 때는 리스트의 index 메소드를 사용하고, index로 찾은 인덱스를 self에 지정하고 새 값을 할당