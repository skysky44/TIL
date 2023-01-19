numbers = []
for _ in range(7):
    num = int(input())
    numbers.append(num)

odd = [i for i in numbers if i % 2 != 0]
if len(odd) == 0:
    print(-1)
else:
    sum_odd = sum(odd)
    min_odd = min(odd)
    print(sum_odd, min_odd, sep='\n')
