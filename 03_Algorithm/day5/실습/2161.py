from collections import deque
# N = int(input())
# nums = [n for n in range(1, N+1)]
# new_nums = []
# while len(nums) > 1:
#     new_nums.append(nums.pop(0))
#     nums.append(nums.pop(0))

# print(*new_nums, *nums)

# popleft로 다시풀기
N = int(input())
nums = deque([n for n in range(1, N+1)])
new_nums = []
while len(nums) > 0:
    print(nums.popleft(), end=' ')
