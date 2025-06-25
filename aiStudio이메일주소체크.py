# aiStudio이메일주소체크.py

import re

def is_valid_email(email):
    """
    정규 표현식을 사용하여 이메일 주소의 유효성을 검사합니다.

    Args:
        email (str): 검사할 이메일 주소 문자열

    Returns:
        bool: 이메일 형식이 유효하면 True, 그렇지 않으면 False를 반환합니다.
    """
    # 이메일 주소를 위한 정규 표현식 패턴
    # [로컬 파트]@[도메인 파트] 형식
    # 로컬 파트: 영문 대소문자, 숫자, 그리고 일부 특수문자(._%+-]) 허용
    # 도메인 파트: 영문 대소문자, 숫자, 하이픈(-) 허용, 마지막 TLD는 2글자 이상의 영문
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # re.match()는 문자열의 처음부터 정규식과 매치되는지 조사합니다.
    # 패턴이 이메일 문자열 전체와 일치해야 하므로, match() 결과가 있는지 확인합니다.
    if re.match(pattern, email):
        return True
    else:
        return False

# --- 테스트를 위한 10개의 샘플 이메일 ---
sample_emails = [
    # --- 유효한 이메일 샘플 (5개) ---
    "test.user@example.com",
    "user_name+alias@sub.domain.co.kr",
    "hello-world@example.net",
    "12345@google.com",
    "my.email@my-company.org",

    # --- 유효하지 않은 이메일 샘플 (5개) ---
    "plainaddress",          # '@'와 도메인이 없음
    "@missing-local.com",    # '@' 앞에 내용이 없음
    "user.name@.com",        # 도메인이 '.'으로 시작함
    "user.name@domain.c",    # 최상위 도메인(TLD)이 너무 짧음
    "user name@domain.com"   # 로컬 파트에 공백 포함
]

# 샘플 이메일들을 하나씩 검사하고 결과 출력
print("--- 이메일 유효성 검사 결과 ---")
for email in sample_emails:
    if is_valid_email(email):
        print(f"'{email}': \t\t[유효함]")
    else:
        print(f"'{email}': \t\t[유효하지 않음]")