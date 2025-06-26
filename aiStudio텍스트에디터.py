import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog, QPlainTextEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class TextViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 텍스트를 표시할 QPlainTextEdit 위젯 생성
        # QPlainTextEdit은 일반 텍스트에 최적화되어 있어 대용량 파일에 더 효율적입니다.
        self.textEdit = QPlainTextEdit()
        self.textEdit.setReadOnly(True)  # 읽기 전용으로 설정
        self.setCentralWidget(self.textEdit)

        # 메뉴 바 생성
        self.create_menu_bar()

        # 윈도우 설정
        self.setWindowTitle('간단한 텍스트 뷰어')
        self.setGeometry(300, 300, 800, 600)  # (x, y, 너비, 높이)
        self.show()

    def create_menu_bar(self):
        """메뉴 바를 생성하고 액션을 연결하는 함수"""
        menuBar = self.menuBar()

        # 파일 메뉴
        fileMenu = menuBar.addMenu('파일(&F)') # '&F'는 Alt+F 단축키를 의미

        # '열기' 액션 생성 및 연결
        openAction = QAction('열기(&O)...', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('텍스트 파일을 엽니다.')
        openAction.triggered.connect(self.open_file) # open_file 함수와 연결
        fileMenu.addAction(openAction)

        # 구분선 추가
        fileMenu.addSeparator()

        # '종료' 액션 생성 및 연결
        exitAction = QAction('종료(&x)', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('프로그램을 종료합니다.')
        exitAction.triggered.connect(self.close) # 내장된 close 함수와 연결
        fileMenu.addAction(exitAction)
        
        # 상태 바 생성 (setStatusTip 메시지를 표시하기 위함)
        self.statusBar()

    def open_file(self):
        """파일 열기 대화상자를 띄우고 선택된 파일의 내용을 불러오는 함수"""
        # QFileDialog를 사용하여 파일 선택 대화상자를 엽니다.
        # getOpenFileName은 (파일 경로, 선택된 필터) 튜플을 반환합니다.
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 열기", "", 
                                                   "Text Files (*.txt);;All Files (*)", options=options)

        # 사용자가 파일을 선택한 경우
        if file_name:
            try:
                # 파일을 utf-8 인코딩으로 엽니다. (한글 깨짐 방지)
                with open(file_name, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self.textEdit.setPlainText(content)
                    # 파일 경로를 윈도우 제목에 표시
                    self.setWindowTitle(f'{file_name} - 간단한 텍스트 뷰어')
            except Exception as e:
                # 파일 읽기 중 오류 발생 시 메시지 박스 표시
                QMessageBox.critical(self, "오류", f"파일을 불러오는 중 오류가 발생했습니다:\n{e}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextViewerApp()
    sys.exit(app.exec_())