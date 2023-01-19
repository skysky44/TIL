from collections import Counter
members = ['j', 'k', 'h', 'j']
count = {}

for member in members:
    # if member not in count:
    #     count[member] = 1
    # else:
    #     count[member] += 1
    count[member] = count.get(member, 0)+1  # 간단히 할 수 있다.

print(count)


# 한번에 마법
