# import sys
# sys.stdin = open("input.txt", "r")

# 2047

string = input().upper()
print(string)


# 2025

n = int(input())
result = int(n*(n+1)/2)  # n(n+1)로 작성하면 안됨

print(result)

# # 2025 다른풀이
# n = int(input())
# result = 0
# for i in range(1, n+1):
#     result += i
# print(result)

# 1936

# 가위 1 바위 2 보 3
x, y = map(int, input().split())

game = {}
game[1, 2] = 'B'  # B가 이기는 경우 1
game[2, 3] = 'B'  # B가 이기는 경우 2
game[3, 1] = 'B'  # B가 이기는 경우 3
game[1, 3] = 'A'  # A가 이기는 경우 1
game[2, 1] = 'A'  # A가 이기는 경우 2
game[3, 2] = 'A'  # A가 이기는 경우 3

print(game[x, y])

# 1936 다른 풀이

x, y = map(int, input().split())
# 가위 1 바위 2 보 3

if x == 1 and y == 3:
    print('A')
elif x == 1 and y == 2:
    print('B')
elif x == 2 and y == 3:
    print('B')
elif x == 2 and y == 1:
    print('A')
elif x == 3 and y == 1:
    print('B')
elif x == 3 and y == 2:
    print('A')

# 2027

for i in range(5):
    print('+'*i, '#', '+'*(4-i), sep='')

# 2058

n = map(int, input())
result = 0

for i in n:
    result += i

print(result)

# 2019
n = int(input())
nums = []

for i in range(n+1):
    nums.append(2**i)

print(*nums)
