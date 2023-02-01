# import sys
# input = sys.stdin.readline

N = int(input())

start = 665
nums = []
while len(nums) != N:
    start += 1
    num = str(start)
    for i in range(0, len(num)-2):
        if num[i] == '6' and num[i+1] == '6' and num[i+2] == '6':
            nums.append(num)
            break
print(nums.pop())
