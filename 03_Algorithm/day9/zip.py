matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print(*matrix)
print(list(zip(*matrix)))
# 전치
# 1 5 9
# 2 6 10
# 3 7 11
# 4 8 12

print(list(zip(*matrix[::-1])))
# 오른쪽 90도 회전
# 9 5 1
# 10 6 2
# 11 7 3
# 12 8 4
