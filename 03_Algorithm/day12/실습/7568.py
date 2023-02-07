N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]
result = []
for x, y in people:
    cnt = 0
    for p, q in people:
        if x < p and y < q:
            cnt += 1
    result.append(cnt+1)
print(*result)
