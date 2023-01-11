# 문제 1

import sys
sys.stdin = open("input.txt", "r")

numbers = list(map(int, input().split()))

print(*numbers)

# 문제 2

sys.stdin = open("input.txt", "r")

string = input().split()

print(*string)

# 문제 3

sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        number = int(input())
        print(number)

# 문제 4
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        number = map(int, input().split())
        print(*number)

# 문제 5
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        string = input().split()
        print(*string)

# 문제 6
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    for _ in range(N):
        number = map(int, input().split())
        print(*number)

# 문제 7
sys.stdin = open("input.txt", "r")

T, N = map(int, input().split())
for t in range(1, T+1):
    for _ in range(N):
        number = int(input())
        print(number)

# 문제 8
sys.stdin = open("input.txt", "r")

T, N = map(int, input().split())
for t in range(1, T+1):
    for _ in range(N):
        number = map(int, input().split())
        print(*number)

# 문제 9
sys.stdin = open("input.txt", "r")

T, N = map(int, input().split())
for t in range(1, T+1):
    for _ in range(N):
        number = map(int, input().split())
        print(*number)
