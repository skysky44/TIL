import heapq

a, b, c = map(int, input().split())
heap = []
for i in a, b, c:
    heapq.heappush(heap, i)

heapq.heappop(heap)
print(heapq.heappop(heap))
