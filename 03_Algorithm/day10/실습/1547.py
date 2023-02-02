import sys
sys.stdin = open('input.txt')
M = int(input())
cup = [1, 0, 0]
for _ in range(M):
    x, y = map(int, input().split())
    cup[x-1], cup[y-1] = cup[y-1], cup[x-1]
print(cup.index(1)+1)
