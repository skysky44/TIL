T = int(input())
for _ in range(T):
    C = int(input())
    coin = [25, 10, 5, 1]
    for c in coin:
        print(C//c, end=' ')
        C = C % c
