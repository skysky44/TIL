matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]

transpose = [[0]*3 for i in range(4)]
print(transpose)

for x in range(3):
    for y in range(4):
        transpose[y][x] = matrix[x][y]

print(transpose)
