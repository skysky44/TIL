# 리스트 사용 풀이
n = int(input())
str_num = input()
result_list = [int(i) for i in str_num]
print(sum(result_list))

# 기존 풀이
n = int(input())
str_num = input()
result = 0
for i in str_num:
    result += int(i)
print(result)
