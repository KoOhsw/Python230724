# Web(웹) - BeautifulSoup 패키지

# 크롤링하기 위한 선언
from bs4 import BeautifulSoup

#Page 로딩 #웹크롤링 폴더 test01.html
page = '''<!DOCTYPE html>
<html>
    <head>
        <title>
            아주 쉬운 HTML문서 샘플입니다.
        </title>
    </head>
    <body>
        <div>
            <p class="inner-text first-item" id="first">
                교육센터
                <a href="http://www.credu.com" id="credu">
                크레듀
                </a>
            </p>
            <p class="inner-text second-item">
                파이썬 사이트
                <a href="https://www.python.org" id="python">
                Python 
                </a>
            </p>
        </div>
        <p class="outer-text first-item" id="second">
            <b>
                데이터 과학은 멋집니다.
            </b>
        </p>
        <p class="outer-text">
            <b>
                지속적인 학습이 필요합니다. 
            </b>
        </p>
    </body>
</html>
'''

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

