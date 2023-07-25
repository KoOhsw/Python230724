# 1)Class정의
class Person:
    #초기화 메서드
    def __init__(self) -> None:
        self.name = 'default name'
    def print(self):
        print('my name is {0}'.format(self.name))

# 2) 인스턴스 생성
p1 = Person()
p2 = Person()

# 3) 메서드 호출
p1.name = '전우치'
p1.print()
p2.print()

#런타임시에 변수 추가
Person.title = 'new title'
print(p1.title)
print(p2.title)
print(Person.title)

print('==== self 누락시 ====')
#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        # 인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        # self 누락
        print(str)
        # self 입력
        print(self.str)

g = GString()
g.set("First Message")
g.print()

print('==== Class 메서드 ====')
class MyClass:
    #초기화 메서드
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
    #소멸자 메서드
    def __del__(self):
        print("Instance is deleted!")
        

c = MyClass(10)

# 언젠가 가비지 컬렉션(GC)에서 메모리를 없앤다
# del을하지 않아도 전체코드종료 후 GC에 의해 del 수행
del c 
print('전체코드종료')


print('==== BankAccount ====')
# BankAccount.py
#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        #클래스 내부에 숨기고 싶다(이름변경)
        self.__id = id
        self.__name = name 
        self.__balance = balance 
    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.deposit(5000)
account1.withdraw(3000)

print(account1)
