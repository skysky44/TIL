T = int(input())

for _ in range(T):
    N = int(input())
    number = map(int, input().split())
    result = sum(number)
    print(result)
