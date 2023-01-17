n = int(input())
first_number = n
count = 0
while True:
    tens = n//10
    units = n % 10
    n = units*10 + (tens+units) % 10
    count += 1
    if first_number == n:
        break
print(count)
