import sys
import pprint

sys.stdin = open('input.txt')
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    # m*n
    grid = []
    for _ in range(m):
        grid.append(input().split())

    # pprint.pprint(grid)
    cnt = 0
    cnt2 = 0
    while True:  # 박스가 아래로 내려갈때까지 반복
        cnt = 0
        for i in range(n):
            for j in range(m-1):
                # 세로로 순회

                if grid[j][i] == '1' and grid[j+1][i] == '0':
                    grid[j][i] = '0'
                    grid[j+1][i] = '1'
                    cnt += 1
        cnt2 += cnt  # while문 끝나는 조건. 더이상 1과 0을 바꾸는 경우가 발생하지 않은 경우에 반복 종료
        if cnt == 0:
            break

    # pprint.pprint(grid)
    print(cnt2)
