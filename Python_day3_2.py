print('==== 정규표현식(RE 모듈) ====')

import re

# 숫자가 0~N번 나오고 th가 있는경우 찾기
result = re.search('[0-9]*th','35th')
print(result)
print(result.group())

result = re.match('[0-9]*th','35th')
print(result)
print(result.group())

# 앞에 공백이 있을경우
result = re.search('[0-9]*th','  35th')
print(result)
print(result.group())

result = re.match('[0-9]*th','  35th')
print(result)
# print(result.group()) //찾을수 없어서 에러발생

result = re.search('apple','빅테크에서 apple의 위상')
print(result.group())

result = re.search('\d{4}','올해는 2023년')
print(result.group())

result = re.search('\d{5}','우리동네는 20233')
print(result.group())

print('-- 대/소문자 --')
data = 'Apple is big compana and apple is very delicioys'
c = re.compile('apple',re.IGNORECASE)
print(c.findall(data))

print('-- 다중라인검색 --')
data2 = '''파이썬을 
배워서

누구나 사용'''
c= re.compile('^.+',re.MULTILINE) # ^.+은 빈줄을 제외하고 전부 가져온다라는 뜻
print(c.findall(data2))
