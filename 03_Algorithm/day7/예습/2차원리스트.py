# 2차원 리스트가 있을 때
# (1) 행 우선 순회
# (2) 열 우선 순회를 직접 한번 해보기 (교재, 파이썬 보지 않고 해보기)
# (3) 이차원 리스트 총합, 최대값
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]

# 1차원 리스트가 있을 때
# [1, 2, 3, 4, 5] => 1칸을 shift한다고 하면 [5, 1, 2, 3, 4]

# 5*5 리스트 만들기
from pprint import pprint
matrix = [[i]*5 for i in range(5)]
pprint(matrix)
# # 행 우선 순회
for i in range(5):
    for j in range(5):
        print(matrix[i][j], end=' ')

# # 열 우선 순회
for i in range(5):
    for j in range(5):
        print(matrix[j][i], end=' ')

# # 이차원 리스트 총합, 최대값
total = 0
max_result = 0
for i in matrix:
    total += sum(i)
    if max_result < max(i):
        max_result = max(i)
print(total, max_result)


# 1차원 리스트가 있을 때
# [1, 2, 3, 4, 5] => 1칸을 shift한다고 하면 [5, 1, 2, 3, 4]
a = [1, 2, 3, 4, 5]
n = 5
for _ in range(n):
    a[1], a[2], a[3], a[4], a[0] = a[0], a[1], a[2], a[3], a[4]
    print(a)
