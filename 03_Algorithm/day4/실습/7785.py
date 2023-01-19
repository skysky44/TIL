# import sys
# input = sys.stdin.readline

n = int(input())
members = {}
for _ in range(n):
    name, state = input().split()
    members[name] = state

for member in sorted(members.keys(), reverse=True):
    if members[member] == 'enter':
        print(member)
