n, x = map(int, input().split())
numbers = list(map(int, input().split()))
result = []
for i in numbers:
    if i < x:
        result.append(i)
for r in result:
    print(r, end=' ')
