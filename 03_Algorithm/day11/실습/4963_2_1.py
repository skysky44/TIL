# 맞은 코드
import sys
sys.setrecursionlimit(10**6)  # 런타임에러 해결
input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def search(grid, x, y):
    if grid[x][y] == 0:  # 0을 만나면 멈춤
        return
    grid[x][y] = 0
    for i in range(8):  # 상하좌우대각선 모두 확인
        if 0 <= x+dx[i] < h and 0 <= y+dy[i] < w:  # 범위안에 있는지 확인
            if grid[x+dx[i]][y+dy[i]] == 1:  # 1이 있다면 0으로 바꿔줌
                grid[x+dx[i]][y+dy[i]] == 0
                search(grid, x+dx[i], y+dy[i])  # 탐색 반복


# 입력을 받아서 인접 행렬로 만들기
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:  # 마지막 0 0 입력 확인
        break
    grid = [list(map(int, input().split())) for _ in range(h)]  # 이차원리스트

# 상하좌우대각선 탐색하고 섬이 몇개인지 cnt
    cnt = 0
    for x in range(h):  # 인접행렬 전체를 순회 한다.
        for y in range(w):
            if grid[x][y] == 1:  # 값이 1이면 0으로 바꿔주고 계속 ..탐색?DFS?
                cnt += 1
                search(grid, x, y)
    print(cnt)
