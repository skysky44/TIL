import sys
sys.stdin = open('input.txt')

n = int(input())
c = int(input())
network = [[] for _ in range(n+1)]  # 컴퓨터 수만큼 빈리스트 만들기
while True:  # 인접리스트 만들기
    try:
        x, y = map(int, input().split())
        network[x].append(y)
        network[y].append(x)
    except:
        break

# DFS

visited = [False]*(n+1)
start = 1
visited[start] = True
stack = []
stack.append(start)

while stack:
    cur = stack.pop()
    for i in network[cur]:
        if not visited[i]:  # False이면 실행
            visited[i] = True
            stack.append(i)

print(sum(visited)-1)  # 1번 걸렸을 때 걸리게 되는 컴퓨터 수
