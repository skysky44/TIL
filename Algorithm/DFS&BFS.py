from collections import deque
N, M, V = map(int, input().split())

# dfs 재귀 사용방법


def dfs(graph, v, visited_dfs):
    # 현재 노드 방문 처리
    visited_dfs[v] = True
    print(v, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited_dfs[i]:
            dfs(graph, i, visited_dfs)
    # print(visited_dfs)

# # dfs stack 사용방법
# def dfs(graph, start, visited_dfs):
#     stack = [start]
#     # 스택이 빌 때까지 반복
#     while stack:
#         v = stack.pop()
#         # 현재 노드가 아직 방문되지 않았다면,
#         if not visited_dfs[v]:
#             # 현재 노드를 방문 처리하고 출력합니다.
#             visited_dfs[v] = True
#             print(v, end=' ')
#             # 현재 노드와 연결된 노드들 중에서,
#             # 아직 방문되지 않은 노드들을 스택에 넣습니다.
#             for i in reversed(graph[v]):
#                 if not visited_dfs[i]:
#                     stack.append(i)


# bfs 큐 사용 방법
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

# # bfs 재귀사용방법
# def dfs(graph, v, visited_dfs):
#     visited_dfs[v] = True
#     print(v, end=' ')

#     for i in graph[v]:
#         if not visited_dfs[i]:
#             dfs(graph, i, visited_dfs)


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
