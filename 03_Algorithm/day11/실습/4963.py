import sys
sys.stdin = open('input.txt')
# 미완성
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 마지막 0 0 입력 확인
        break

    grid = [list(map(int, input().split())) for _ in range(h)]  # 인접행렬
    adj_list = [[] for _ in range(h+1)]  # 인접리스트로 변경

    for x in range(h):  # 이차원리스트를 인접리스트로 바꾸기
        for y in range(w):
            if grid[x][y] == 1:
                adj_list[x].append(y)
    print(adj_list)
    # visited가 모두 True가 될 때까지 DFS 반복?
    visited = [False]*(h+1)
    cnt = 0
    while visited.count(False) != 0:  # visited가 모두 True면 멈춤//while 한번 끝나면 섬 하나?
        for i in range(h+1):
            if visited[i] == False:  # visited에서 False인 것만 꺼내서 DFS 실행
                start = i
                visited[start] = True
                stack = []
                stack.append(start)
                while stack:
                    cur = stack.pop()
                    for i in adj_list[cur]:
                        if not visited[i]:  # False이면 실행
                            visited[i] = True
                            stack.append(i)
                print(visited)
                print(stack)
                cnt += 1
    print(cnt)
