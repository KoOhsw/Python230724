# 1)Class정의
class Person:
    #초기화 메서드
    def __init__(self) -> None:
        self.name = 'default name'
    def print(self):
        print('my name is {0}'.format(self.name))

# 2) 인스턴스 생성
p1 = Person()
# 3) 메서드 호출
p1.print()