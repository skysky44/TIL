# 예제 1
list_variable = [0, 1, 2, 3, 4, 5, 6]
list_variable.pop()
list_variable.append(7)
list_variable.append(8)

for element in list_variable[2:]:  # 리스트변수[시작인덱스:종료인덱스:step]

    print(element, end=" ")


"""
예측을 작성하세요.
2 3 4 5 6 7 8
"""

# 예제 2

for element in range(-2, 10, 2):
    print(element, end=" ")

"""
예측을 작성하세요.
-2 0 2 4 6 8
"""

# 예제 3

a, b, c, d = 0, 0, 0, 0
n = 10

for number in range(n):
    if number % 2 == 0:
        a = a + 1

    if number % 3 == 0:
        b = b + 1

    if number % 4 == 0:
        c = c + 1

    if number % 5 == 0:
        d = d + 1

print(a, b, c, d)  # 5 4 3 2
# 0 포함

# 예제 4

i = 0
while i <= 10:
    print(i)
    i = i + 1
"""
예측을 작성하세요.
0
1
3
4
5
6
7
8
9
10
"""

# 예제 5

i = 0
while i <= 10:
    i = i + 1
    print(i)
"""
예측을 작성하세요.
1
2
3
4
5
6
7
8
9
10
11
"""

# 예제 4 예제 5번 순서에 따라 결과값 변화

# 예제 6
i = 0
while i <= 10:
    i = i + 2
    print(i)
"""
예측을 작성하세요.
2
4
6
8
10
12
"""

# 예제 7

i = 0
while True:
    print(i)
    i = i + 1
    if i > 10:
        break
"""
예측을 작성하세요.
0
1
2
3
4
5
6
7
8
9
10
"""

# 예제 8

i = 0
while True:
    print(i)
    if i > 10:
        break
    i = i + 1

"""
예측을 작성하세요.
0
1
2
3
4
5
6
7
8
9
10
11
"""

# 예제 9

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(len(list_variable))  # 7

# 예제 10

list_variable = [0, 1, 2, 3, 4, 5, 6]
print(sum(list_variable))  # 21

# 예제 11

list_variable = [3, 1, 4, -3, 9, 7]
print(min(list_variable) - max(list_variable))  # -12
