# import sys
import heapq
# sys.stdin = open('input.txt')

w = []
k = []
score_w = []
score_k = []

for _ in range(10):
    heapq.heappush(w, -int(input()))
for _ in range(10):
    heapq.heappush(k, -int(input()))

for _ in range(3):
    score_w.append(-heapq.heappop(w))
    score_k.append(-heapq.heappop(k))


print(sum(score_w), sum(score_k))
