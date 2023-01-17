# n = int(input())
# numbers = map(int, input().split())
# total = 0
# score = 0
# for number in numbers:
#     if number == 1:
#         score += 1
#         total += score
#     else:
#         score = 0

# print(total)

n = int(input())
numbers = list(map(int, input().split()))
total = 0
score = 0
cnt = 0
while cnt < n:
    if numbers[cnt] == 1:
        score += 1
        total += score
        cnt += 1
    else:
        score = 0
        cnt += 1

print(total)
