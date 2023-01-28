remainder = []
for _ in range(10):
    n = int(input())
    remainder.append(n % 42)
set_remainder = set(remainder)
print(len(set_remainder))
