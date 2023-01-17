n = int(input())
num_list = []
for _ in range(n):
    num_list.append(int(input()))
print(*sorted(num_list), sep='\n')
