# import sys
# sys.stdin = open('input.txt')
N = int(input())
pi = list(map(int, input().split()))
height = 0
max_height = 0
for i in range(N-1):
    if pi[i] < pi[i+1]:
        height += pi[i+1]-pi[i]
        if max_height < height:
            max_height = height
    elif pi[i] >= pi[i+1]:
        if max_height < height:
            max_height = height
        height = 0
print(max_height)
