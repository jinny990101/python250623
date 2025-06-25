# ChatGPT코스피200.py

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_index.naver?code=KPI200"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

print("#1:",soup)

# box_type_m div에서 type_1 테이블 추출
box = soup.find("div", class_="box_type_m")
if box is None:
    print("box_type_m 클래스를 찾을 수 없습니다.")
    exit()

table = box.find("table", class_="type_1")
if table is None:
    print("type_1 테이블을 찾을 수 없습니다.")
    exit()

rows = table.find_all("tr")

for row in rows:
    cols = row.find_all("td")
    if len(cols) == 7:
        # 종목명 추출 (a 태그 내부 텍스트)
        name = cols[0].find("a").get_text(strip=True) if cols[0].find("a") else cols[0].get_text(strip=True)
        price = cols[1].get_text(strip=True)
        # 전일비는 <span> 태그 내부 텍스트
        change = cols[2].find("span").get_text(strip=True) if cols[2].find("span") else cols[2].get_text(strip=True)
        rate = cols[3].get_text(strip=True)
        volume = cols[4].get_text(strip=True)
        amount = cols[5].get_text(strip=True)
        marketcap = cols[6].get_text(strip=True)
        print(f"종목명: {name}, 현재가: {price}, 전일비: {change}, 등락률: {rate}, 거래량: {volume}, 거래대금: {amount}, 시가총액: {marketcap}")

