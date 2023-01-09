# 문제 1
# 문자열을 입력받고, e 가 처음 나오는 위치(index)를 출력하세요.
# 만약, 문자열에서 e 가 없으면 -1 을 출력하세요.

string = input('문자열을 입력하세요 > ')
for i in range(len(string)):
    if string[i] == 'e':
        print(i)
        break
else:  # for문 끝까지 반복하면 -1 출력(for-else)
    print(-1)

# 문제 2
# 문자열을 입력받고, 각 단어의 등장 횟수를 출력하세요.

strings = input('문자열을 입력하세요 > ').split()
dict_string = {}
for string in strings:
    if string not in dict_string:
        dict_string[string] = 1
    else:
        dict_string[string] += 1

for key, value in dict_string.items():
    print(key, value)

# 문제 3
# 문자열을 입력받고, e 를 제거한 결과를 출력하세요.

string = list(input('문자열을 입력하세요 > '))
for i in string:
    if i == 'e':
        string.remove(i)
print(*string, sep='')

# 문제 4
# 문자열과 알파벳을 공백으로 구분해서 입력받고, 문자열에서 입력한 알파벳의 개수를 출력하세요.

strings, alphabet = input('문자열을 입력하세요 > ').split()
cnt = 0
for string in strings:
    if string == alphabet:
        cnt += 1
print(cnt)

# 문제 5
# 단어 3개를 입력받고, 3개의 단어를 - 로 연결해서 출력하세요.

a, b, c = input('문자열을 입력하세요 > ').split()
print(a, b, c,  sep='-')

# 문제 6
# 양의 정수를 입력받고, 자리수의 합을 출력하세요.
# 만약, 입력 받은 값이 0보다 작으면 -1을 출력하세요.
# 단, 양의 정수를 문자열로 변경하지마세요. str() 함수를 사용하지마세요.

number = int(input('양의 정수를 입력하세요 > '))
result = 0
if number < 0:
    print(-1)
else:
    while number != 0:
        result += number % 10
        number = number//10
    print(result)
