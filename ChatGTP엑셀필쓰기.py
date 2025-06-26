import random
from openpyxl import Workbook

# 전자제품명 샘플 리스트
product_names = [
    "노트북", "스마트폰", "태블릿", "스마트워치", "모니터",
    "키보드", "마우스", "프린터", "스피커", "헤드폰"
]

wb = Workbook()
ws = wb.active
ws.title = "제품목록"

# 헤더 작성
ws.append(["제품ID", "제품명", "가격", "수량"])

for i in range(1, 101):
    product_id = f"P{i:04d}"
    name = random.choice(product_names)
    price = random.randint(50000, 2000000)  # 5만원~200만원
    quantity = random.randint(1, 100)
    ws.append([product_id, name, price, quantity])

wb.save("productList_ChatGPT.xlsx")