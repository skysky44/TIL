import heapq
N = int(input())
words = []
for _ in range(N):
    words.append(input())

heap = []
words = list(set(words))
# 같은 단어 여러번 입력된 경우 한번씩만 출력- set()
heapq.heapify(words)
# 문자열을 요소로 가진 리스트를 heap정렬 하면
# 사전순으로 정렬이 됨(?)

for word in words:
    heapq.heappush(heap, (len(word), word))

for _ in range(len(heap)):
    print(heapq.heappop(heap)[1])
