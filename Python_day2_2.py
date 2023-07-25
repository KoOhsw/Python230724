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

#_클래스이름__속성명으로 접근이 가능하다 => 완벽하게 숨길수 없다...
#account1._BankAccount__balance = 1500000
#print(account1._BankAccount__balance)
print(account1)

print('==== 상속 ====')
class Person:
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
    
    def working(self):
        print('현재 작업중')
    
    def coding(self):
        print('현재 코딩중')


class Student(Person):
    #상속받고 덮어쓰기(재정의, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print('Info(Subject:{0}, StudentID : {1}'.format(self.subject,self.studentID))

#인스턴스 생성
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "빅데이터", "201234")

# print(p.__dict__)
# print(s.__dict__)

p.printInfo()
s.printInfo()
s.coding()
s.working()