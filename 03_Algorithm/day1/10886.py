n = int(input())
not_cute = 0
cute = 0
for _ in range(n):
    i = int(input())
    if i == 0:
        not_cute += 1
    else:
        cute += 1

if not_cute > cute:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')
