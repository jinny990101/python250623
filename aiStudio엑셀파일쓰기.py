import openpyxl
import random

# 1. 새 엑셀 워크북(Workbook) 생성
try:
    wb = openpyxl.Workbook()
    # 활성화된 시트(Sheet) 선택
    ws = wb.active
    # 시트 이름 변경
    ws.title = "전자제품 목록"

    # 2. 헤더(Header) 추가
    headers = ["제품ID", "제품명", "가격", "수량"]
    ws.append(headers)

    # 3. 데이터 생성을 위한 샘플 목록 정의
    product_types = ["스마트폰", "노트북", "태블릿", "모니터", "키보드", "마우스", "헤드폰", "스마트워치", "TV", "스피커", "웹캠", "프린터"]
    brands = ["삼성", "LG", "Apple", "Sony", "Dell", "HP", "Logitech"]
    model_suffixes = ["Pro", "Air", "Ultra", "Plus", "Standard", "Gaming", "Slim"]

    # 4. 100개의 데이터 행 생성 및 추가
    print("100개의 전자제품 데이터를 생성 중입니다...")
    for i in range(1, 101):
        # 제품ID 생성 (예: PROD-001, PROD-002, ...)
        product_id = f"PROD-{str(i).zfill(3)}"

        # 제품명 랜덤 조합
        product_name = f"{random.choice(brands)} {random.choice(product_types)} {random.choice(model_suffixes)} {random.randint(100, 999)}"

        # 가격 랜덤 생성 (50,000원 ~ 3,000,000원 사이, 1000원 단위)
        price = random.randint(50, 3000) * 1000

        # 수량 랜덤 생성 (0 ~ 100개)
        quantity = random.randint(0, 100)

        # 생성된 데이터를 리스트 형태로 시트에 추가
        ws.append([product_id, product_name, price, quantity])

    # 5. 너비 자동 조절 (선택 사항)
    for column_cells in ws.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        ws.column_dimensions[column_cells[0].column_letter].width = length + 2


    # 6. 엑셀 파일 저장
    file_name = "productList_aiStudio.xlsx"
    wb.save(file_name)

    print(f"'{file_name}' 파일이 성공적으로 생성되었습니다. (총 100개의 데이터 포함)")

except Exception as e:
    print(f"오류가 발생했습니다: {e}")