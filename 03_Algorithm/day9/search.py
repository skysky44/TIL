x = 1
y = 1
# 행을 x 열을 y로 표현(또는 행을 r 열을 c)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 상
nx = x + dx[0]
ny = y + dy[0]
# 하
nx = x + dx[1]
ny = y + dy[1]
# 좌
nx = x + dx[2]
ny = y + dy[2]
# 우
nx = x + dx[3]
ny = y + dy[3]

for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

# 상하좌우 튜플로도 가능

# 이동 후 범위 확인, 끝 부분, 엣지 확인
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위 안에 있으면 갱신하기(3*3 행렬 기준)
    if 0 <= nx < 3 and 0 <= ny < 3:
        x = nx
        y = ny
