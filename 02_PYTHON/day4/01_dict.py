# 전화번호부
# 키 - 이름(상호명)
# 값 - 전화번호
phone_book = {
    '피자헛': '1588-5588',
    '전화번호': '114',
    '김탁희': '010-1233-1233',
    '대리운전': '1577-1577'
}

# print(phone_book['피자헛'])

for name in phone_book:
    # 키 순회
    print(name)
    # 값 순회
    print(phone_book[name])
