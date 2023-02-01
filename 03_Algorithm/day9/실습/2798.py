# import sys
# sys.stdin = open('input.txt')
n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = []
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):  # range 범위 주의..
            total = cards[i]+cards[j]+cards[k]
            if m >= total:
                result.append(total)
print(max(result))
