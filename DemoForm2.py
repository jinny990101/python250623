# DemoForm2.py
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#디자인문서를 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]
#윈도우 클래스 정의
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self) # UI 설정
        self.label.setText("안녕하세요! 파이썬Qt")
    #슬롯메서드 추가
    def firstClick(self):
        self.label.setText("첫번째 버튼이 클릭")
    def secondClick(self):
        self.label.setText("두번째 버튼이 클릭했음")
    def thirdClick(self):
        self.label.setText("세번째 버튼이 클릭했음~~")


#진입점체크
if __name__ == "__main__":
    app = QApplication(sys.argv) # QApplication 객체 생성
    demoForm = DemoForm() # DemoForm 클래스의 인스턴스 생성
    demoForm.show() # 윈도우를 화면에 표시
    app.exec_() # 이벤트 루프 시작