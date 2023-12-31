# DemoForm.py PyQt
# DemoForm.ui(화면단) + DemoForm.py(로직단) - 현재파일

import sys
from PyQt6.QtWidgets import *
from PyQt6 import uic

# 디자인된 문서 로딩
form_class = uic.loadUiType('Python_day4_7.ui')[0]

# 폼클래스 정의
class DemoForm(QDialog, form_class):
    #초기화 메서드(생성자)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText('First Screen')

# 직접 모듈을 실행했는지 체크
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demoForm = DemoForm()
    demoForm.show()
    app.exec()
