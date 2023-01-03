# 문제 1
num = int(input('정수를 입력하세요 > '))
if num > 0:
    print(True)
else:
    print(False)

# 문제 2

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))
if a == b:
    print(False)
elif a > b:
    print(a)
elif a < b:
    print(b)

# 문제 3

num = int(input('정수를 입력하세요 > '))
if 1 < num < 10:
    print(True)
else:
    print(False)

# 문제 4

num = int(input('정수를 입력하세요 > '))
if num > 0 and num % 2 == 0:
    print(True)
else:
    print(False)

# 문제 5
num = int(input('정수를 입력하세요 > '))
if num > 100 or num < 0:
    print('에러')
elif num >= 60:
    print('합격')
else:
    print('불합격')

# 문제 6

strings = input('문자열을 입혁하세요 > ')
for string in range(len(strings)-1, -1, -1):
    print(strings[string])


# 문제 7
a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
elif a > b:
    for i in range(b+1, a):
        print(i)
elif a < b:
    for i in range(a+1, b):
        print(i)

문제 8

a = int(input('첫 번째 정수를 입력하세요 > '))
b = int(input('두 번째 정수를 입력하세요 > '))

if a == b:
    print(False)
elif a > b:
    for i in range(a-1, b, -1):
        print(i, end=" ")
elif a < b:
    for i in range(b-1, a, -1):
        print(i, end=" ")

# 문제 9

a = int(input('정수를 입력하세요 > '))

if a >= 1:
    for i in range(1, a, 2):
        print(i)
else:
    print(False)

# 문제 10
for i in range(2, 10):
    for j in range(2, 10):
        print(f'{i} X {j} = {i*j}')
