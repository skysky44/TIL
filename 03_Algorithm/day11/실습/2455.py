# import sys
# sys.stdin = open('input.txt')

passenger = 0
max_passenger = 0
for _ in range(4):
    off, on = map(int, input().split())
    passenger = passenger - off + on
    if passenger > max_passenger:
        max_passenger = passenger

print(max_passenger)
