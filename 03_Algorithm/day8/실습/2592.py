import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

nums = {}
total = 0
for _ in range(10):
    num = int(input())
    total += num
    nums[num] = nums.get(num, 0) + 1

print(int(total/10))
print(sorted(nums.items(), key=lambda x: x[1], reverse=True)[0][0])
