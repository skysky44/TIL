import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    # x 가 0 아니면 배열에 x 를 추가
    if x != 0:
        if x < 0:
            x = (-x, x)
        else:
            x = (x, x)
        heapq.heappush(heap, x)
    # x 가 0 이면 배열에서 절댓값이 가장 작은 값을 출력하고
    # 그 값을 배열에서 제거
    else:
        if heap:
            print(heapq.heappop(heap)[1])
    # 배열이 비어있는 경우 x가 0 이면 0 출력
        else:
            print(0)
