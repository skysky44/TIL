from collections import deque
N = int(input())
customer = deque(list(map(int, input().split())))
result = []
cnt = 0
for n in range(N):
    a = customer.popleft()
    if a not in result:
        result.append(a)
    else:
        cnt += 1
print(cnt)
