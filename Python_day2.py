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

    