# MyProduct.ui(화면단) + ProductList3.py(로직단)
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic 
import sqlite3
import os.path

# 데이터베이스 처리 클래스
class ProductDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        self._init_db()

    def _init_db(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.con.commit()

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def get_all_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 처리 클래스
form_class = uic.loadUiType("MyProduct.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.db = db

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.prodID.setReadOnly(True)  # ID는 자동생성, 수정불가

        # 엔터키로 다음 컨트롤 이동
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())

        # 버튼 시그널 연결
        self.pushButton.clicked.connect(self.getProduct)      # 검색
        self.pushButton_2.clicked.connect(self.addProduct)    # 입력
        self.pushButton_3.clicked.connect(self.updateProduct) # 수정
        self.pushButton_4.clicked.connect(self.removeProduct) # 삭제

        # 더블클릭 시그널
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 초기 데이터 로딩
        self.getProduct()

    def addProduct(self):
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격(숫자)을 올바르게 입력하세요.")
            return
        self.db.add_product(name, int(price))
        self.getProduct()
        self.prodName.clear()
        self.prodPrice.clear()

    def updateProduct(self):
        prod_id = self.prodID.text().strip()
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        if not prod_id or not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "수정할 항목을 선택하고, 제품명과 가격(숫자)을 올바르게 입력하세요.")
            return
        self.db.update_product(int(prod_id), name, int(price))
        self.getProduct()

    def removeProduct(self):
        prod_id = self.prodID.text().strip()
        if not prod_id:
            QMessageBox.warning(self, "선택 오류", "삭제할 항목을 선택하세요.")
            return
        self.db.remove_product(int(prod_id))
        self.getProduct()
        self.prodID.clear()
        self.prodName.clear()
        self.prodPrice.clear()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.get_all_products()
        self.tableWidget.setRowCount(len(products))
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        row = self.tableWidget.currentRow()
        self.prodID.setText(self.tableWidget.item(row, 0).text())
        self.prodName.setText(self.tableWidget.item(row, 1).text())
        self.prodPrice.setText(self.tableWidget.item(row, 2).text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = ProductDB(r"C:/work/sqlite3/ProductList.db")
    myWindow = Window(db)
    myWindow.show()
    sys.exit(app.exec_())



