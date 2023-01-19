taebo = input()
left_cnt = 0
right_cnt = 0
for i in taebo:
    if i == '@':
        left_cnt += 1
    elif i == '0':
        break

for i in taebo[::-1]:
    if i == '@':
        right_cnt += 1
    elif i == '0':
        break

print(left_cnt, right_cnt)
