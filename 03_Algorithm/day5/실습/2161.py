N = int(input())
nums = [n for n in range(1, N+1)]
new_nums = []
while len(nums) > 1:
    new_nums.append(nums.pop(0))
    nums.append(nums.pop(0))

print(*new_nums, *nums)
