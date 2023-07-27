# Web(웹) - BeautifulSoup 패키지

# 크롤링하기 위한 선언
from bs4 import BeautifulSoup

#Page 로딩
page = open('c:\\work\\웹크롤링\\test01.html','rt', encoding='utf-8').read()

#검색이 용이한 객체 생성
soup = BeautifulSoup(page, 'html.parser')

#페이지보기 
#print(soup.prettify)

#<p> 전체를 검색
#print(soup.find_all('p'))

#<p> 하나를 검색
#print(soup.find('p'))

#<p class='outer-text'> 조건검색
#print(soup.find_all('p',class_='outer-text'))
 
#속성(attrs:Attributies) 이용 검색
#print(soup.find_all('p', attrs = {'class':'outer-text'}))

#id 검색
#print(soup.find_all(id='first'))

#태그 내부 문자열 가져오기(.text속성)
for tag in soup.find_all('p'):
    title = tag.text.strip()
    title = title.replace('\n','')
    print(title)

