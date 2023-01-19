T = int(input())
for _ in range(T):
    result = ''
    num, word = input().split()
    for i in word:
        result += i*int(num)
    print(result)
