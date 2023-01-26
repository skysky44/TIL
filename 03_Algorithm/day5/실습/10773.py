K = int(input())
nums = []
for k in range(K):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))
