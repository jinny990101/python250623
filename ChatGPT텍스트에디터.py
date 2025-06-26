import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QFileDialog, QVBoxLayout, QWidget

class TextViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("텍스트 파일 뷰어")
        self.setGeometry(200, 200, 600, 400)

        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)

        self.openButton = QPushButton("파일 열기", self)
        self.openButton.clicked.connect(self.openFile)

        layout = QVBoxLayout()
        layout.addWidget(self.openButton)
        layout.addWidget(self.textEdit)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def openFile(self):
        filePath, _ = QFileDialog.getOpenFileName(self, "텍스트 파일 선택", "", "Text Files (*.txt);;All Files (*)")
        if filePath:
            try:
                with open(filePath, 'r', encoding='utf-8') as f:
                    text = f.read()
            except UnicodeDecodeError:
                with open(filePath, 'r', encoding='utf-16') as f:
                    text = f.read()
            self.textEdit.setPlainText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = TextViewer()
    viewer.show()
    sys.exit(app.exec_())