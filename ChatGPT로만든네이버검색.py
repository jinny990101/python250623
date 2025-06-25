# ChatGPT로만든네이버검색.py

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

query = "이란"  # 검색어
url = f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={query}"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목과 링크 추출
news_items = soup.select('a.BHYkUbEQ2afEbTC7LXoA.tQzTN_dJmfJcpqVyJEAz, a.BHYkUbEQ2afEbTC7LXoA.Ba1Kt4dKXms6CvCOZyFl')

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active
ws.title = "네이버뉴스"
ws.append(["번호", "제목", "링크"])

for idx, item in enumerate(news_items, 1):
    title = item.get_text(strip=True)
    link = item['href']
    ws.append([idx, title, link])

wb.save("result.xlsx")
print("result.xlsx 파일로 저장됨.")

