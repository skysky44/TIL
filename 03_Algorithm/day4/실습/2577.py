# 풀이1
abc = 1
for i in range(3):
    i = int(input())
    abc *= i

num_dic = {}
for i in str(abc):
    num_dic[i] = num_dic.get(i, 0)+1

for i in range(0, 10):
    print(num_dic.get(str(i), 0))

# # 풀이 1 개선 전
# a = int(input())
# b = int(input())
# c = int(input())
# mul = a*b*c
# num_dic = {
#     '0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0,
#     '6': 0, '7': 0, '8': 0, '9': 0

# }
# for i in str(mul):
#     num_dic[i] = num_dic.get(i)+1
# for value in num_dic.values():
#     print(value)


# from collections import Counter
# mul_itmes = Counter(str(mul))
# print(mul_itmes)
