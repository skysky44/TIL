import sys
sys.stdin = open('input.txt')

N = int(input())
room = []
for _ in range(N):
    s = list(input())
    room.append(s)

cnt1 = 0  # 가로 기준 . 의 수
cnt2 = 0  # 가로로 누울 자리 수
for i in range(N):
    for j in range(N):
        if room[i][j] == '.':
            cnt1 += 1
            if cnt1 == 2:
                cnt2 += 1
        elif room[i][j] == 'X':
            cnt1 = 0
    else:
        cnt1 = 0

cnt3 = 0  # 세로 기준 .의 수
cnt4 = 0  # 세로로 누울 자리의 수
for i in range(N):
    for j in range(N):
        if room[j][i] == '.':
            cnt3 += 1
            if cnt3 == 2:
                cnt4 += 1
        elif room[j][i] == 'X':
            cnt3 = 0
    else:
        cnt3 = 0
print(cnt2, cnt4)


# 실패 코드

# cnt1 = 0
# for i in range(N):
#     for j in range(N-1):
#         if room[i][j] == '.' and room[i][j+1] == '.':
#             cnt1 += 1
#             break

# cnt2 = 0
# for i in range(N):
#     for j in range(N-1):
#         if room[j][i] == '.' and room[j+1][i] == '.':
#             cnt2 += 1
#             break
# print(cnt1, cnt2)
