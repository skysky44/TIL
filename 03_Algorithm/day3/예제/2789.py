word = input()
new_word = ''
for i in word:
    if i not in 'CAMBRIDGE':
        new_word += i
print(new_word)


# word = input()
# new_word = []
# for i in word:
#     if i not in 'CAMBRIDGE':
#         new_word.append(i)
# for j in new_word:
#     print(j, end='')
