nums = list(map(int, input().split()))

while True:
    for i in range(4):
        if nums[i] > nums[i+1]:
            nums[i+1], nums[i] = nums[i], nums[i+1]
            print(*nums)
    if nums == [1, 2, 3, 4, 5]:
        break
