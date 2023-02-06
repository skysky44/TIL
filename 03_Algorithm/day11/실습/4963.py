import sys
sys.stdin = open('input.txt')
# 미완성
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 마지막 0 0 입력 확인
        break

    grid = [list(map(int, input().split())) for _ in range(h)]  # 이차원리스트
    adj_list = [[] for _ in range(h+1)]  # 인접리스트로

    for x in range(h):  # 이차원리스트를 인접리스트로 바꾸기
        for y in range(w):
            if grid[x][y] == 1:
                adj_list[x].append(y)

    # visited가 모두 True가 될 때까지 DFS 반복?
    visited = [False]*(h+1)
    cnt = 0
    while sum(visited) != h+1:  # visited가 모두 True면 멈춤
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
                cnt += 1
    print(cnt)
