# 회전

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
# m*n
m = 3
n = 4
rotate = [[0]*m for i in range(n)]
print(rotate)

# 왼쪽 90도(어렵)
for i in range(m):
    for j in range(n):
        rotate[n-1-j][i] = matrix[i][j]
print(rotate)

# 오른쪽 90도
for i in range(m):
    for j in range(n):
        rotate[j][m-i-1] = matrix[i][j]
print(rotate)
