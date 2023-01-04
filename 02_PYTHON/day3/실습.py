# 1부터 양의 정수까지 합 while문
a = 0
b = int(input('양의 정수 입력하세요 > '))
total = 0
while a < b:
    a = a+1
    total = total+a
print(total)


a = 1
b = int(input('양의 정수 입력하세요 > '))
total = 0
while a <= b:
    total = total+a
    a = a+1
    print(total, a)
print(total)

# for 문
n = int(input('양의 정수 입력 '))
total = 0
for i in range(1, n+1):
    total = total + i

print(total)
