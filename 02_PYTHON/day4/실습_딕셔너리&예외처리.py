# 문제1
# 문자열을 입력 받고 문자열에서 e 의 개수를 구해서 출력하세요.

word = input('문자열을 입력하세요 > ')
cnt = 0
for i in word:
    if i == 'e':
        cnt += 1
print(cnt)

# 문제2
# 문자열을 입력 받고, 문자열 중 알파벳 모음의 총 개수를 출력하세요.

word = input('문자열을 입력하세요 > ')
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
cnt = 0
for i in word:
    for j in vowels:
        if i == j:
            cnt += 1
print(cnt)

# 문제 3
dict_variable = {
    "이름": "정우영",
    "생년": "2000",
    "회사": "하이퍼그로스",
}
age = 2023 - int(dict_variable["생년"]) + 1
print(f'나이 : {age}세')

# 문제 4
# 이름, 전화번호, 거주지 정보를 입력받아 딕셔너리 구조로 저장하고, 해당 딕셔너리와 딕셔너리의 정보를 구분해서 출력하세요.

name = input("이름을 입력하세요 > ")
phone_num = input("전화번호를 입력하세요 > ")
address = input("거주지를 입력하세요 > ")
dict_variable = {"이름": name, "전화번호": phone_num, "거주지": address}
print(dict_variable)
for key, value in dict_variable.items():
    print(f'{key} : {value}')  # 다른 방법은 없나요

# 문제 5
# 이름, 전화번호, 이메일, 거주지 정보를 입력받아 출력 예시와 동일한 딕셔너리 구조를 출력하세요.
name = input("이름을 입력하세요 > ")
phone_num = input("전화번호를 입력하세요 > ")
email = input("이메일을 입혁하세요 > ")
address = input("거주지를 입력하세요 > ")

dict_variable = {name: {'전화번호': phone_num, '이메일': email, '거주지': address}}
print(dict_variable)

# 문제6
# 문자열을 입력받고, 문자열에서 개별 문자가 나오는 횟수를 출력하세요.
word = input("문자열을 입력하세요 > ")
dict_word = {}
for i in word:
    if i not in dict_word:  # dict_word 안에 i key가 없으면
        dict_word[i] = 1  # key 추가하고 value 로 1
    else:
        dict_word[i] = dict_word[i] + 1  # 있으면 value에 +1????

for key in dict_word:
    print(key, dict_word[key])
