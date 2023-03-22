from collections import deque
N, M, V = map(int, input().split())


def dfs(graph, v, visited_dfs):
    # 현재 노드 방문 처리
    visited_dfs[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)
    # print(visited_dfs)


def bfs(graph, start, visited_bfs):
    queue = deque([start])
    # 현재노드 방문처리
    visited_bfs[start] = True
    # 큐가 빌때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited_bfs[i]:
                queue.append(i)
                visited_bfs[i] = True


graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    i.sort()
# print(graph)

visited_dfs = [False]*(N+1)
dfs(graph, V, visited_dfs)
print()
visited_bfs = [False]*(N+1)
bfs(graph, V, visited_bfs)
