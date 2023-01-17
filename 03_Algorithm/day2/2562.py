numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)
x = max(numbers)
th = numbers.index(x)
print(x, th+1, sep='\n')
