# MainWindow.py PyQt 당큰마켓 크롤링과 연계
# MainWindow.ui(화면단) + MainWindow.py(로직단) - 현재파일

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 웹통신
import requests
# 크롤링
from bs4 import BeautifulSoup


# 디자인된 문서 로딩
form_class = uic.loadUiType('MainWindow.ui')[0]

# 폼클래스 정의
class DemoForm(QMainWindow, form_class):
    #초기화 메서드(생성자)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('버튼을 클릭하세요')

    #슬롯 메서드 추가
    def firstClick(self):
        url = "https://www.daangn.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        posts = soup.find_all('div', attrs={'class':'card-desc'})

        f = open('c:\\work\\dangn.txt','wt',encoding='utf-8')
        for post in posts:
            title = post.find('h2', attrs = {'class':'card-title'})
            price = post.find('div', attrs = {'class':'card-price'})
            addr = post.find('div', attrs = {'class':'card-region-name'})

            title =title.text.replace('\n','')
            price =price.text.replace('\n','')
            addr =addr.text.replace('\n','')

            print(f'{title},{price},{addr}')
            f.write(f'{title},{price},{addr}\n')
        f.close()        
        #-----------------------
        self.label.setText('당근마켓 크롤링 완료')
    def secondClick(self):
        self.label.setText('두번째 버튼을 클릭')
    def thirdClick(self):
        self.label.setText('세번째 버튼을 클릭')

# 직접 모듈을 실행했는지 체크
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec_()

