N = int(input())
result = 4
for num in range(4, N+1):
    for i in str(num):
        if i not in ['4', '7']:
            break
    else:
        if result < num:
            result = num

print(result)
