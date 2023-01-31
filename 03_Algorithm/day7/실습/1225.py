a, b = map(str, input().split())

a_mat = [int(i) for i in a]
b_mat = [int(j) for j in b]
print(sum(a_mat)*sum(b_mat))


# # 시간초과

# a, b = map(str, input().split())

# result = 0
# a_mat = [int(i) for i in a]
# b_mat = [int(j) for j in b]

# for i in range(len(a_mat)):
#     for j in range(len(b_mat)):
#         result += (a_mat[i]*b_mat[j])
# print(result)
