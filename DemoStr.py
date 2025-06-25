# DemoStr.py

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(strA.capitalize())  # 첫 글자만 대문자로
print(len(strA))  # 문자열 길이
print(len(strB))  # 문자열 길이
print("MBC2580".isalnum())  # 알파벳과 숫자로만 구성되어 있는지 확인
print("2580".isdecimal())  # 숫자로만 구성되어 있는지 확인

data = "<<<   spam and ham     >>>"
result = data.strip("<> ")  # 양쪽 공백 제거
print(data)
print(result)       
result2 = result.replace("spam", "spam egg")  # 문자열 치환
print(result2)  # 치환된 문자열 출력
lst = result2.split()  # 문자열을 공백으로 분리하여 리스트로 변환
print(lst)  # 리스트 출력
print(" ".join(lst))  # 리스트를 공백으로 연결하여 문자열로 변환


#정규표현식을 사용
import re

result = re.search("[0-9]*th", "  35th")
print("search:",result)
print(result.group())  # 정규표현식 검색 결과 출력

result = re.match("[0-9]*th", "  35th")
print("match:",result)
# print(result.group())  # 정규표현식 매칭 결과 출력  

result = re.search("\d{4}", "올해는 2025년입니다.")
print(result.group())

result = re.search("\d{5}", "가격은 12340000원 입니다.")
print(result.group())  # "12340"이 포함된 문자열에서 검색 결과 출력

result = re.search("apple", "This is apple")
print(result.group())  # "apple"이 포함된 문자열에서 검색 결과 출력


