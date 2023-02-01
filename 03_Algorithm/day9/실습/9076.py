# import sys
from collections import deque
# sys.stdin = open('input.txt')
T = int(input())
for _ in range(T):
    score = sorted(list(map(int, input().split())))
    score = deque(score)

    score.popleft()
    score.pop()

    if abs(score[0] - score[-1]) >= 4:
        print('KIN')
    else:
        print(sum(score))
