# Python_day2.py

print('==== 함수 정의2 ====')
x=1
def func(a):
    return a+x
print(func(1))
#지역변수가 있을경우 지역변수 우선 Local -> Global -> Built in 순 조회
def func2(a):
    x=5
    return a+x
print(func2(1))

#기본값 지정-초기값 지점
def times(a=10,b=20):
    return a*b
print(times())
print(times(5))
print(times(5,6))
print(times(b=10))

#키워드 인자
def connectURI(server,port):
    strURL = 'http://' + server + ':' + port
    return strURL

print(connectURI('credu.com','80'))
print(connectURI(port = '8080', server = 'credu.com'))

print('==== 함수 정의3 ====')
#가변인자
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union('HAM','SPAM'))
print(union('HAM','SPAM','EGG'))


#람다 함수
print('==== 람다 함수 ====')
g = lambda x,y : x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

print('==== 내장함수 필터 ====')
def getBiggerThan20(i):
    return i>20
lst = [10,25,30]
iterL = filter(getBiggerThan20,lst)
for i in iterL:
    print(i)

print('==== 람다 이용 ====')
iterL = filter(lambda x:x>20,lst)
for i in iterL:
    print(i)

#분기구문
# 선택한 블럭 주석처리 : Ctrl + /
# print('==== 분기구문 ====')
# score = int(input('Input Score:'))

# if 90 <= score <= 100:
#     grade = 'A'
# elif 80 <= score <90:
#     grade = 'B'
# elif 70 <= score <80:
#     grade = 'C'
# else:
#     grade = 'D'

# print('Grade is ',grade)

print('==== 반복구문 ====')
value = 5
while value >0:
    print (value)
    value -=1

lst = [100,'str',3.14]
for i in lst:
    print(i)

print('==== Break ====')
lst = list(range(1,11))
for i in lst:
    if i>5:
        break
    print('Item:{0}'.format(i))

print('==== Continue ====')
lst = list(range(1,11))
for i in lst:
    if i % 2 == 0:
        continue
    print('Item:{0}'.format(i))

print('==== Range함수 ====')
print(list(range(2010,2024,2)))

print('====  리스트 컴프리헨션 ====')
lst = list(range(1,11))
print( [i**2 for i in lst if i>5])
tp = ('apple', 'banana', 'orange')
print( len(i) for i in tp)
d = {100:'apple', 200:'kiwi'}
print([v.upper() for v in d.values()])

for i in map(lambda x:x+10,lst):
    print(i)
