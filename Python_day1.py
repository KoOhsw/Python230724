# Python_day1.py

#Indexing
#[시작:끝]으로 문자열 인덱싱, 슬라이싱이 가능
#시작이 처음부터라면 생략O, 끝이 마지막 까지라면 생략O
print('====문자열 인덱싱====')
strA = 'python is very powerful'
print(strA[0])
print(strA[1])
print(strA[0:3])
print(strA[:3])
print(strA[-3:])
print(strA[-8:])

#List 관련
print('==== 리스트 ====')
colors = ['red','blue','green']
print(colors)
print(len(colors))
print(colors[0])

# for구문의 반복구간은 들여쓰기한 구간까지로 적용된다
# 들여쓰기가 문법에 사용되므로 주의가 필요하다
for item in colors:
    print(item)

colors.append('white')
print(colors)
colors.insert(1,'pink')
print(colors)
print(colors.index('red'))

# 에러는 나지 않지만 'r','e','d'로 추가 된다
# 단어 추가를 원할때는 사용하면 안되는 잘못된 문법이다.
colors += 'red'
print(colors.pop())
print(colors.pop())
print(colors.pop())

print(colors.pop(1))

print(colors)

colors.extend(['black','red','white','pink'])
print(colors)

colors.remove('black')
print(colors)

colors.sort()
print(colors)

colors.reverse()
print(colors)

# Set 관련
print('==== 세트 ====')
a = {1,2,3,3}
b = {3,4,4,5}

print(a)
print(type(a))
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

# Tuple 관련
print('==== 튜플 ====')
tp = (10,20,30)
print(len(tp))
print(tp[0])
print('id:%s, name:%s' %('kim','김유신'))

# 함수정의
def calc(a,b):
    return a+b,a*b
# 함수호출
retValue = calc(5,6)
print(retValue)

print('==== 형식변환 ====')
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
c = tuple(b)
print(c)

#Dict 관련
print('==== 딕셔너리 ====')
dic_color =  {'apple':'red','banana':'yellow'}
print (len(dic_color))
print(dic_color['apple'])
dic_color['cherry'] = 'red'
print(dic_color)

device ={'iphone':5,'galaxy':10,'window':30}

#key를 검색하여 value 출력
print(device['iphone'])

#Dict 자료 추가
device['macbook'] = 15
print(device)

#Dict 자료 수정
device['iphone'] = 6
print(device)

#Dict 자료 삭제
del device['iphone']
print(device)

for item in device.items():
    print(item)

for key in device.keys():
    print(key)

for value in device.values():
    print(value)

print('==== 딕셔너리2 ====')
# 이름 + 전화번호 맵핑
phone = {'kim':'1111','lee':'2222','park':'3333'}
print (phone.values())
print ('kim' in phone) # 검색은 key로만 가능하다

# 원본은 하나이고 참조형식으로 동작한다
# 따라서 p에 추가 했지만 phone에도 추가된다
p = phone
print(id(p),id(phone)) 
p['kang'] = '4444'
print(phone) 

print('==== 논리형식 ====')
isRight = True
print(type(isRight))
print(1<2)
print(1!=2)
print(1 ==2)
print(True and True)
print(True and False)
print(True or False)

print('==== 함수정의 ====')
#리턴하지 않아도 함수 구현이 다능하다
def setValue(newValue):
    x = newValue
    print('지역변수:',x)
#강제로 리턴받아서 출력하면 None 출력(아무것도 없음)
result = setValue(5)
print(result)

def swap(x,y):
    return y,x

print(swap(3,4))

#교집합 문자를 리턴하는 함수
def intersect(prelist, postlist):
    #local
    result =[]
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

print(intersect('HAM','SPAM'))
print('test')