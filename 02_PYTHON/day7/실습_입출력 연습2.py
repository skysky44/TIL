# 문제 1
number = int(input())
print(number)

# 문제 2
string = input().split()
print(*string)

# 문제 3
T = int(input())

for t in range(1, T+1):
    print(input())
    pass

# 문제 4

numbers = list(map(int, input().split()))

print(*numbers)

# 문제 5

a, b = list(map(int, input().split()))

print(a, b)

# 문제 6
stirng = input().split()

print(*stirng)

# # 문제 7
# T = int(input())
# for t in range(1, 15, 3):
#     print(t, t+1, t+2)
# 이거인 줄 알았어요..
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(*numbers)


# 문제 8
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(*numbers)
