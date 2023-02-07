import sys
sys.stdin = open('input.txt')

input = sys.stdin.readline
N = int(input())
bar = [int(input()) for _ in range(N)]
count = 0
check = 0
for height in reversed(bar):
    if height > check:
        check = height
        count += 1
print(count)
