# ChatGPT이메일주소체크.py
import re

def is_valid_email(email):
    # 간단한 이메일 정규식 패턴
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# 샘플 이메일 10개
sample_emails = [
    "test@example.com",
    "user.name@domain.co.kr",
    "user_name123@sub.domain.com",
    "user-name@domain.io",
    "user+name@domain.org",
    "invalid-email@",
    "noatsign.com",
    "user@.com",
    "user@domain",
    "user@domain.c"
]

for email in sample_emails:
    result = "유효함" if is_valid_email(email) else "유효하지 않음"
    print(f"{email}: {result}")


