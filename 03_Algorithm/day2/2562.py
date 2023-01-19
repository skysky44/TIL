numbers = []
for _ in range(9):
    num = int(input())
    numbers.append(num)
x = max(numbers)
th = numbers.index(x)
print(x, th+1, sep='\n')


# max랑 index 통을 만들어서 풀 수 있음
