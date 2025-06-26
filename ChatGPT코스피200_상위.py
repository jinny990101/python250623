import sys
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import re
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QLabel, QMessageBox
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal

def clean_number(text):
    """숫자 문자열에서 쉼표를 제거하고 정수로 변환"""
    if isinstance(text, str):
        return re.sub(r'[^\d.-]', '', text)
    return text

def get_kospi200_top_stocks(max_pages=10):
    """
    네이버 금융에서 코스피200 편입종목 상위 데이터를 크롤링
    
    Args:
        max_pages: 크롤링할 최대 페이지 수 (기본값: 10)
    
    Returns:
        DataFrame: 코스피200 편입종목 데이터
    """
    base_url = "https://finance.naver.com/sise/entryJongmok.naver"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    
    all_data = []
    
    for page in range(1, max_pages + 1):
        try:
            params = {
                "type": "KPI200",
                "page": page
            }
            
            response = requests.get(base_url, params=params, headers=headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 편입종목 상위 테이블 찾기
            table = soup.find("table", class_="type_1")
            if not table:
                continue
                
            rows = table.find_all("tr")
            
            for row in rows:
                cols = row.find_all("td")
                if len(cols) == 7:  # 유효한 데이터 행인지 확인
                    stock_name = cols[0].get_text(strip=True)
                    current_price = cols[1].get_text(strip=True)
                    
                    # 전일비 추출 (상승/하락/보합 구분)
                    change_elem = cols[2].find("span", class_="tah")
                    change = change_elem.get_text(strip=True) if change_elem else "0"
                    
                    # 상승/하락/보합 상태 확인
                    status = None
                    if cols[2].find("em", class_="bu_pup"):
                        status = "상승"
                    elif cols[2].find("em", class_="bu_pdn"):
                        status = "하락"
                    elif cols[2].find("em", class_="bu_pn"):
                        status = "보합"
                    
                    change_rate = cols[3].get_text(strip=True)
                    volume = cols[4].get_text(strip=True)
                    amount = cols[5].get_text(strip=True)
                    market_cap = cols[6].get_text(strip=True)
                    
                    # 종목 코드 추출 (종목 링크에서)
                    stock_link = cols[0].find("a")
                    stock_code = None
                    if stock_link and 'href' in stock_link.attrs:
                        code_match = re.search(r'code=(\d+)', stock_link['href'])
                        if code_match:
                            stock_code = code_match.group(1)
                    
                    all_data.append({
                        "종목코드": stock_code,
                        "종목명": stock_name,
                        "현재가": current_price,
                        "전일비": change,
                        "상태": status,
                        "등락률": change_rate,
                        "거래량": volume,
                        "거래대금(백만)": amount,
                        "시가총액(억)": market_cap
                    })
            
            time.sleep(0.5)  # 너무 빠른 요청은 차단될 수 있으므로 잠시 대기
            
        except Exception as e:
            print(f"페이지 {page} 크롤링 중 오류 발생: {e}")
    
    if not all_data:
        return pd.DataFrame()
    
    # DataFrame 생성 및 데이터 전처리
    df = pd.DataFrame(all_data)
    
    # 숫자 데이터 전처리
    numeric_columns = ['현재가', '전일비', '거래량', '거래대금(백만)', '시가총액(억)']
    for col in numeric_columns:
        df[col] = df[col].apply(clean_number)
    
    # 등락률에서 퍼센트 기호 제거
    df['등락률'] = df['등락률'].str.replace('%', '').astype(float)
    
    # 날짜 및 시간 정보 추가
    df['수집일시'] = pd.Timestamp.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return df

class CrawlerThread(QThread):
    result = pyqtSignal(pd.DataFrame)
    def __init__(self, max_pages=10):
        super().__init__()
        self.max_pages = max_pages
    def run(self):
        df = get_kospi200_top_stocks(self.max_pages)
        self.result.emit(df)

class Kospi200Viewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("코스피200 종목 뷰어")
        self.setGeometry(100, 100, 1100, 600)

        # 검색창, 버튼
        self.searchEdit = QLineEdit(self)
        self.searchEdit.setPlaceholderText("종목명 또는 코드로 검색")
        self.searchButton = QPushButton("검색", self)
        self.reloadButton = QPushButton("새로고침", self)

        topLayout = QHBoxLayout()
        topLayout.addWidget(QLabel("검색:"))
        topLayout.addWidget(self.searchEdit)
        topLayout.addWidget(self.searchButton)
        topLayout.addWidget(self.reloadButton)

        # 테이블
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "종목코드", "종목명", "현재가", "전일비", "상태", "등락률", "거래량", "거래대금(백만)", "시가총액(억)"
        ])
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setAlternatingRowColors(True)

        # 전체 레이아웃
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(topLayout)
        mainLayout.addWidget(self.tableWidget)

        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        # 데이터
        self.df = pd.DataFrame()
        self.searchButton.clicked.connect(self.search)
        self.reloadButton.clicked.connect(self.reloadData)
        self.searchEdit.returnPressed.connect(self.search)

        self.reloadData()

    def reloadData(self):
        self.searchButton.setEnabled(False)
        self.reloadButton.setEnabled(False)
        self.tableWidget.setRowCount(0)
        self.df = pd.DataFrame()
        self.thread = CrawlerThread(max_pages=10)
        self.thread.result.connect(self.displayData)
        self.thread.start()

    def displayData(self, df):
        self.df = df
        self.showTable(self.df)
        self.searchButton.setEnabled(True)
        self.reloadButton.setEnabled(True)
        if df.empty:
            QMessageBox.warning(self, "알림", "데이터를 불러오지 못했습니다.")

    def showTable(self, df):
        self.tableWidget.setRowCount(len(df))
        for row, item in enumerate(df.itertuples(index=False)):
            for col, value in enumerate(item):
                self.tableWidget.setItem(row, col, QTableWidgetItem(str(value)))
        self.tableWidget.resizeColumnsToContents()

    def search(self):
        keyword = self.searchEdit.text().strip()
        if self.df.empty:
            return
        if not keyword:
            self.showTable(self.df)
            return
        filtered = self.df[
            self.df['종목명'].str.contains(keyword, case=False, na=False) |
            self.df['종목코드'].astype(str).str.contains(keyword, na=False)
        ]
        self.showTable(filtered)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = Kospi200Viewer()
    viewer.show()
    sys.exit(app.exec_())