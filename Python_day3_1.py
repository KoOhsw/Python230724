# 입출력
for i in range(0,10):
    url = 'http://www.credu.com/?page='+str(i)
    print(url)

print('==== 오른쪽 정렬 ====')
for x in range(100,106):
    print(x,"*",x,'=', '{0:,}'.format(x*x).rjust(7))

print('==== 0 채우기 ====')
for x in range(1,6):
    print(x,'*',x,'=',str(x*x).zfill(5))

print('==== 서식지정 ====')
print('{0:x}\n{1:b}\n{2:,}\n{3:e}\n{4:f}\n{5:,.2f}'.format(10,10,1500,4/3,4/3,1500 + 4/3))

import os
fpath = os.getcwd()
print('==== 파일 입출력 ====')
# 파일 쓰기
f = open(fpath + '\\day3_1.txt','wt',encoding='utf-8')
f.write('First\nSecond\nThird')
f.close()

# 파일읽기
f = open(fpath + r'\day3_1.txt','rt',encoding='utf-8')
result = f.read()
print('-- 전체읽기 --')
print(result)
print('-- 라인단위 --')
f.seek(0)
print(f.readline(), end='')
print(f.readline(), end='')
print('-- 리스트 받기 --')
f.seek(0)
result = f.readlines()
print(result)

f.close()

print('==== Str 클래스 ====')
#print(dir(str))

strA = '파이썬은 강력해'
strB = 'python is very powerful'

print(len(strA))
print(len(strB))
print(strB.capitalize())
print('-- 문자 개수 세기 --')
print(strB.count('p'))
print(strB.count('p',7))
print('-- 시작/끝 문자 확인 --')
print(strB.startswith('python'))
print(strB.endswith('ful'))
print('-- 대/소문자 바꾸기 --')
# 특정메서드는 원본데이터를 변경하지는 않는다 ->> 리턴받아서 활용 또는 바로 활용한다.
result = strB.upper()
print(result)
result2 = result.lower()
print(result2)

print('-- 공백제거 --')
data = '<<   spam and ham >>'
result = data.strip('<> ')
print(data)
print(result)

print('-- 문자 치환 --')
result2 = result.replace('spam','spam egg')
print(result2)

print('-- 문자 나누기 --')
lst = result2.split()
print(lst)
data2 = 'spam::ham::egg'
result3 = data2.split('::')
print(result3)

print('-- 문자 합치기 --')
print(':)'.join(lst))

print('-- 문자열 체크 --')
print('MBC2580'.isalnum())  # 알파벳 + 숫자?
print('MBC:2580'.isalnum()) # 알파벳 + 숫자?
print('A2580'.isdecimal())  # 순수 숫자?


