# 문제 1
# 정수 한 개를 입력 받고, 해당 정수의 절대값을 출력하세요.

n = int(input('정수를 입력하세요 > '))
if n > 0:
    print(n)
elif n < 0:
    print(-n)
else:
    print(0)

# 문제 2
# 리스트 요소의 개수를 출력하세요.
number_list = [1, 2, 3, 4, 5]
count = 0
for number in number_list:
    count += 1
print(count)

number_list = []
count = 0
for number in number_list:
    count += 1
print(count)

# 문제 3
# 리스트에 저장된 정수들의 합을 출력하세요.

number_list = [1, 2, 3, 4, 5]
list_sum = 0
for number in number_list:
    list_sum += number
print(list_sum)

number_list = [-1, -2, -3, -4, -5]
list_sum = 0
for number in number_list:
    list_sum += number
print(list_sum)

# 문제 4
# 리스트에 저장된 정수들의 평균을 출력하세요

number_list = [2, 4, 6]
cnt = 0
number_sum = 0
for number in number_list:
    number_sum += number
    cnt += 1
print(number_sum/cnt)

number_list = [2, 3, 5, 7]
cnt = 0
number_sum = 0
for number in number_list:
    number_sum += number
    cnt += 1
print(number_sum/cnt)

# 문제 5
# 리스트에 저장된 정수들의 곱을 출력하세요.

number_list = [1, 2, 3, 4, 5]
result = 1

for number in number_list:
    result *= number

print(result)

number_list = [-1, -2, 3]
result = 1

for number in number_list:
    result *= number

print(result)

# 다른 방식
# a, b, c, d, e = map(int, number_list)
# print(a*b*c*d*e)

# 문제 6
# 리스트에 저장된 정수 중 가장 큰 값을 출력하세요.

number_list = [1, 2, 3, 4, 5]
max_number = number_list[0]
for n in range(len(number_list)):
    if number_list[n] >= max_number:
        max_number = number_list[n]
print(max_number)

# 최종
number_list = [1, 2, 3, 4, 5]
max_number = number_list[0]
for n in number_list:
    if n >= max_number:
        max_number = n
print(max_number)


number_list = [1, 1, 1]
max_number = number_list[0]
for n in range(len(number_list)):
    if number_list[n] >= max_number:
        max_number = number_list[n]
print(max_number)

# 최종
number_list = [1, 1, 1]
max_number = number_list[0]
for n in number_list:
    if n >= max_number:
        max_number = n
print(max_number)

# 문제 7
# 리스트에 저장된 정수 중 가장 작은 값을 출력하세요.

number_list = [1, 2, 3, 4, 5]
min_number = number_list[0]
for n in number_list:
    if n <= min_number:
        min_number = n
print(min_number)

number_list = [5, 5, 5, 2]
min_number = number_list[0]
for n in number_list:
    if n <= min_number:
        min_number = n
print(min_number)
