a_num, b_num = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(len(a ^ b))
