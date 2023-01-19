alphabet = input()
second = 0
phone_dic = {
    # '1': 1,
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
    # '0': 10
}
for i in alphabet:
    second += phone_dic[i]+1
print(second)


# # 미완성
# alphabet = input()
# second = 0
# phone_dic = {}
# key2 = ['A', 'B', 'C']
# key3 = ['D', 'E', 'F']
# key4 = ['G', 'H', 'I']
# key5 = ['J', 'K', 'L']
# key6 = ['M', 'N', 'O']
# key7 = ['P', 'Q', 'R', 'S']
# key8 = ['T', 'U', 'V']
# key9 = ['W', 'X', 'Y', 'Z']
# for i in range(2, 10):
#     phone_dic += dict.fromkeys(f'key{i}', i)

# print(phone_dic)

# for i in alphabet:
#     second += phone_dic[f'key{i}']+1
# print(second)

# # keys = ['a', 'b', 'c', 'd']
# # y = dict.fromkeys(keys, 100)
# # # y={'a': 100, 'b': 100, 'c': 100, 'd': 100}
