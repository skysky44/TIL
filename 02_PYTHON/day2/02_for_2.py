a = 'pineapple'

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print('=======')

for char in a:
    print(char)

print('=======')

# 1. 반복 가능한 객체 : 각 요소가 필요할 때

for i in range(5):
    print(a[i])

print('=======')

# 2. 반복 가능한 객체 : 인덱스가 필요할 때

for i in range(len(a)):
    print(a[i])
