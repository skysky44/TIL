# 2029
T = int(input())
for t in range(1, T+1):
    a, b = list(map(int, input().split()))
    quotient = a // b
    remainder = a % b
    print(f'#{t} {quotient} {remainder}')

# 2071
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    average = sum(numbers)/len(numbers)
    result = round(average)  # 반올림
    print(f'#{t} {result}')

# 1938
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)  # 소수점이하 버림

# (a+b,'\n',a-b,'\n',a*b,'\n',a//b)

# 1938 다른 코드
a, b = map(int, input().split())
calculation = [a+b, a-b, a*b, a//b]
for result in calculation:
    print(result)


# 2046
n = int(input())
print('#'*n)

# 2068
T = int(input())
for t in range(1, T+1):
    numbers = list(map(int, input().split()))
    result = max(numbers)
    print(f'#{t} {result}')
