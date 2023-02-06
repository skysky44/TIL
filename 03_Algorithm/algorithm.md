# 알고리즘 1일차

## 알고리즘 공부

- 어려운 문제일수록 생각하는 시간 필요
- 개발자란? 문제해결을 하는 사람(기술을 좀 아는)
- 오랜 시간 고민했는데 풀리지 않을 때 타인의 답을 보면서 나에게 적합한 풀이를 찾는 것이 좋다.

- a라고 하는 문제를 다른 알고리즘으로 접근할 때가 있음(시간복잡도)
- 지금레벨: 코드 테크닉 x, 일반적인 접근 방법
- 90~95% : 문자열/리스트
- 5~10% : 딕셔너리, 세트

- 반복적으로 다른 사람 코드와 비교하다 보면 눈에 들어올 것

- 300 ~ 350문제 / solved.ac 참고

- 니클라우스 비르트 . 튜링상 수상
- 프로그램 == 데이터구조(저장) + 알고리즘(조작)

## 데이터 구조& 알고리즘

- Array (배열)
- Linked List (연결리스트)
- Hash (해시)
- Stack (스택)
- Queue (큐)
- Priority Queue (우선순위 큐)
- Heap(힙)
- Tree (트리)
- Graph (그래프)

- 기본 : 완전 탐색, 재귀, 시뮬레이션, 그리디
- 심화 : DFS, BFS, 백트래킹, 이진탐색, DP, 다익스트라, 크루스칼,프림

## 참고

- map 반복가능한 요소를 형변환 한다.
- 디버거 사용법 : number(변수)가 3일때 멈춤 가능/ 언제 어디에 찍어야 하느냐가 중요

# 알고리즘 2일차

## 시간복잡도(Time Complexity)

- 개인의 컴퓨터 환경에 따라 같은 알고리즘도 측정시간이 달라 객관적인 기준이 필요
- 알고리즘 내부에서 기본연산이 몇 번 일어나는지 확인

- 시간복잡도: (단순하게) `알고리즘의 수행 시간`을 의미

## 빅오(Big-O) 표기법

- 입력 n이 무한대로 커진다고 가정하고 최고차항만 남김(최악의 경우 고려)
- 정확한 수치보다는 증가율에 초점

![image](https://blog.kakaocdn.net/dn/s0pox/btq6Mbphdwr/s5K0D58hi5hiSrBuxmHHwk/img.png)

- O(1) < O(logN) < O(N) < O(NlogN) < O(N^2) < O(N^3) < O(2^N)< O(N!)
- O(logN) : input size를 N이라고 했을때 `N*(1/2)^k = 1`(N을 1로 만들어주는 k값을 구하는 것) 그래서 `k = logN`

## 리스트(List)

### 배열(Array)

- 여러 데이터들이 연속된 메모리 공간에 저장되어 있는 자료구조
- 인덱스를 통해 데이터에 빠른 접근
- 배열의 길이는 변경 불가능(길이 변경하고 싶으면 새로 생성)
- 데이터 타입은 고정

### 연결리스트(Linked List)

- 데이터가 담긴 여러 노드들이 순차적으로 연결된 형태의 자료구조
- 맨 처음 노드부터 순차적 탐색
- 연결리스트의 길이는 자유롭게 변경 가능
- 다양한 데이터 타입 저장
- 데이터가 메모리에 연속적으로 저장되지 않음

### 파이썬의 리스트

- 인덱스로 접근(배열) + 가변 길이(연결리스트)

- 파이썬 리스트의 메서드

```python
.append()
.pop() # .pop(): 마지막 원소 pop / .pop(i): 인덱스i 원소 pop
.count()
.index() # 처음(왼쪽부터)으로 원소가 등장하는 인덱스 반환
.sort() # 오름차순 정렬(revese=True 옵션으로 내림차순 정렬)
.revese()
```

- 주의: .pop 하면 기존리스트가 바꾸기 때문에 for문 결과가 달라짐!

- 자주 쓰이는 리스트 관련 내장함수

```python
len()
sum()
max()
min()
sorted() : # 오름차순으로 새로운 리스트 반환(원본 리스트 변화 없음)
reversed() # 거꾸로 뒤집은 새로운 객체 반환(원본 리스트 변화 없음)
```

## 리스트 컴프리헨션(List Comprehension, 리스트 내포)

- 의미: 리스트를 생성하는 간단한 방법

```python
numbers=[]
for i in range(5):
    numbers.append(i)
```

- 간단하게

```python
numbers = [i for i in range(5)]
```

- if문으로 필터링도 가능

```python
odd numbers = [i for i range(10) if i % 2 ==1]
# [1, 3, 5, 7, 9]
```

# algorithm 3일차

## 문자열(String)

- 변경 불가능(immutable): 바꾸고 싶다면 새로 만드는 방식으로

### 문자열조작

- 문자열 슬라이싱

```
s[start:end:step]
```

- 뒤에서부터 N개 : s[-N:] 또는 [len(s) - N:](???)
- s[:] 전체의미
- s[::-1] 역순

### 문자열 메서드

- .split() : 문자열을 일정 `기준`으로 나누어 `리스트`로 반환

- .strip() : 문자열 양쪽 끝의 특정 문자를 모두 제거한 새로운 문자열 반환(''공백 제거, 'abc' a,b,c 해당문자 모두제거)

- .find() : 처음 나타나는 위치(인덱스) 반환, 없으면 -1

- .index() : 처음 나타나는 위치(인덱스) 반환, 없으면 오류

- .count() : 몇개인지

- .replace() : 기존 문자를 새로운 문자로 치환, '' 특정문자를 빈문자열로 수정(삭제 효과)

- .join : iterable의 각각 원소사이에 특정 문자를 삽입한 새로운 문자열 반환. 공백출력, 콤마 출력 등 원하는 출력 형태를 위해 사용 ex) ','.join(words)

### 아스키(ASCII) 코드

- 알파벳을 표현하는 대표 인코딩 방식
- 각 문자 표현 1byte(8bits) 사용
- ord(문자): 문자 -> 아스키코드
- chr(아스키코드): 아스키코드 -> 문자

### 참고

- 문자열 패턴일치/정규표현식 regular expression?

- a = apple
- 'a'로 시작하는지 알고 싶음 a[0] == 'a'
- ap로 시작하는지 알고 싶음 : a[:2] == 'ap'
- 길이가 N인 문자로 시작하는지 알고 싶음
- a.startswith('a')
- a.endswith('e')

# algorithm 4일차

## 딕셔너리(Dictionary)

### 해시 테이블

- 파이썬에는 딕셔너리 자료구조가 내장 되어있다.
- Non-sequence, key-value, key는 immutable(변경불가능)
- 해시 알고리즘 : 자료 탐색할 때 사용
- `딕셔너리`는 해시함수와 해시 테이블 이용하기 때문에 삼입, 삭제, 수정, 조회 `연산의 속도가 리스트보다 빠르다`.

### 딕셔너리 활용

- 어떤 문자를 기준으로 무언가를 찾고 싶을 때
- key, value 구조로 관리 해야하는 경우
- 데이터에 대한 빠른 접근 탐색 필요한 경우

### 딕셔너리 기본 문법

```python
# 선언
변수={key1: value1,key2:value2}
# 삽입/수정(해당key 있으면 수정 없으면 삽입)
딕셔너리[key]=value
# 삭제
딕셔너리.pop(key)
딕셔너리.pop(key, default) # 해당 key 없으면 default 나옴
# 조회
딕셔너리[key]
딕셔너리.get(key.default) # 해당 key 없으면 default 나옴
```

### 딕셔너리 메서드

- .keys() : `key 목록`이 담긴 `dict_keys` 객체 반환
- .values() : `value 목록`이 담긴 `dict_values` 객체 반환
- .items() : `(key,value)`쌍 목록 담긴 `dict_items`객체 반환

## 참고

- Collections Counter
- 반복가능한 무언가를 넣으면 딕셔너리로 만들어 줌

# 알고리즘 5일차

- 프로그램 = 데이터구조 + 알고리즘
- 자료를 어떻게 저장하고 활용(조작, CRUD)할 것인가.

## 스택(Stack)

- LIFO(last in first out, 후입선출)
- top에서 push 하고 pop이 이루어짐
- 사용 예시
  - 이전 작업의 기억(뒤집기, 되돌리기, 뒤로가기)
  - 괄호매칭(여는 괄호를 다 담고 pop해서 닫는 괄호와 맞으면 ok)
  - 함수호출(재귀 호출), 백트래킹, DFS(깊이 우선 탐색)
- 파이썬 리스트에서 append, pop, a[-1](top 의미)

```python
K = int(input())
nums = []
for k in range(K):
    num = int(input())
    if num == 0:
        nums.pop()
    else:
        nums.append(num)
print(sum(nums))
```

## 큐(Queue)

- 한쪽 끝에서 데이터를 넣고 다른 한쪽 끝에서 데이터를 빼는 구조
- FIFO(first in first out, 선입선출)
- dequeue: 큐 맨앞 데이터 가져오는 행위
- enqueue: 큐 맨뒤 데이터 삽입하는 행위
- 사용 예시
  - 순서와 대기
  - 프로세스 관리(데이터 버퍼)
  - 클라이언트/서버(Message Queue)
  - BFS(너비 우선 탐색), 다익스트라 - 우선순위큐
- 파이썬 리스트에서 pop(0), append() 사용
- 파이썬은 `pop(0)(시간복잡도 O(n))` 대신 내장 된 collections의 depue의 `popleft(시간 복잡도 O(1))` 빠르게 사용 가능

```python
from collections import deque
N = int(input())
customer = deque(list(map(int, input().split())))
result = []
cnt = 0
for n in range(N):
    a = customer.popleft()
    if a not in result:
        result.append(a)
    else:
        cnt += 1
print(cnt)
```

## 참고&팁

- 문제 풀이에서 최근 것이 필요하거나 순서대로 꺼내야하면 큐 스택 생각 해보기
- 딕셔너리에서 items 사용해서 키-값으로 조작 가능(둘 다 동시에)
- in 'string' 으로 하나씩 확인 가능

# 알고리즘 6일차

## 우선순위 큐(Priority Queue)

- 우선순위(중요도, 크기 등 순서 이외의 기준)를 기준으로 가장 우선순위가 높은 데이터가 먼저 나가는 방식
- dequeue: 큐의 맨 앞 데이터를 가져오는 행위
- enqueue: 큐의 맨 뒤에 데이터를 삽입하는 행위
- 우선 순위 큐를 구현 하는 방법

  1. 배열
  2. 연결리스트
  3. 힙

- 우선 순위 큐 구현 별 시간 복잡도

  ![image](https://user-images.githubusercontent.com/110805149/215793287-2749a06b-c0ea-464f-9a4e-3aa1c72ae6f7.png)

## 힙(Heap)

### 특징

- 최댓값 또는 최솟값을 빠르게 찾아내도록 만들어진 데이터 구조
- 완전 이진 트리로 느슨한 정렬 상태를 지속적으로 유지
- 힙 트리에서는 중복 값 허용

### 사용시기

- 데이터가 지속적으로 정렬되어야 할 때
- 데이터에 삽입/삭제가 빈번할 때

### 파이썬의 heapq 모듈

- Minheap(최소힙)으로 구현 되어 있음
- 삽입, 삭제, 수정, 조회 연산의 속도가 리스트보다 빠름
- 힙과 리스트 시간복잡도
  ![image](https://user-images.githubusercontent.com/110805149/215794547-37dcea90-118f-49a6-beb7-7be722e4f13b.png)

- 큐는 dequeue/enqueue
- 힙은 heapq.heappop()/heapq.heappush()

```python
heapq.heapify()
heapq.heappop(heap)
heapq.heappush(heap, item)
```

## 셋(Set)

### Set 연산

```python
.add() #추가
.remove() #제거
| #합집합
- #차집합
& #교집합
^ #대칭차집합
```

### 사용시기

- 데이터의 중복 삭제
- 정수가 아닌 데이터의 삽입/삭제/탐색이 빈번히 필요할 때(?)

### 시간복잡도

![image](https://user-images.githubusercontent.com/110805149/215796463-49ed0108-6aba-4b2a-bbdf-e4b8603807de.png)

## 참고

- 파이썬에 큐 모듈도 있지만 시간 오래걸려서 데크 모듈 사용
- for-else문
  - for 반복문이 break로 끝나지 않으면 else 블럭 실행
  - for 반복문이 break로 끝나면 else 블록 실행 x
- ctrl + alt + 화살표 : 커서 연속지정
- if heap: 힙이 빈게 아니면 트루
- 힙 요소는 튜플 일 수 있다.
- heap 으로 문자열 리스트를 정렬 하면... heappop 했을 때 아스키코드로 오름차순 나옴

# 알고리즘 7일차

## 이차원 리스트

- 리스트를 원소로 가지는 리스트
- 행렬(matrix)
- 리스트컴프리헨션

```python
matrix = {
    [1,2,3]
    [4,5,6]
    [7,8,9]
}

matrix1=[[0]*m for _ in range(n)]
```

## 참고

- 람다 정렬할 때 키에 튜플로 감싸서 정렬
- 좌표평면 말고 매트릭스 생각하기(가로읽기 미족이 세로부터 생각)
- b = list(a) : 리스트를 리스트로 형변환하면 주소가 달라짐

# 알고리즘 8일차

- 이차원리스트 인덱스 조작(핵심)
  - 순환할 때 인덱스를 리스트 길이로 나눈 나머지라고 하면 됨
    - new[(i+n)%N]= a[i]
  - a[-n:] + a[:-n]
  - deque(흑마법)
    - d.rotate(2)

## 순회

- 인덱스를 통해 순회
- 행 우선 순회/ 열 우선 순회

## 전치

- 행렬의 행과 열을 서로 맞바꾸는 것
- 꼭 빈 매트릭스를 만들어 주고 시작해야함

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
# 빈 매트릭스 꼭 만들기
transpose = [[0]*3 for i in range(4)]

for x in range(3):
    for y in range(4):
        transpose[y][x] = matrix[x][y]
```

## 회전(Rotate)

- 왼쪽 90도 회전, 오른쪽 90도 회전
- N-행-1

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
# m*n
m = 3
n = 4
rotate = [[0]*m for i in range(n)]

# 왼쪽 90도(어렵)
for i in range(m):
    for j in range(n):
        rotate[n-1-j][i] = matrix[i][j]

# 오른쪽 90도
for i in range(m):
    for j in range(n):
        rotate[j][m-i-1] = matrix[i][j]

# for 문 인덱스 만들기 어려움
# zip을 사용하면 쉬움(흑마법)
```

## 참고

- 직사각형 왼쪽 아래 꼭짓점 기준으로 넒이 파악 가능

  - 2차원리스트 활용하는 방법
  - 점을 set 에 넣고 중복제거 하고 set 길이 출력

- sum(map(sum, ... )) 사용가능

# 알고리즘 9일차

## 완전탐색(Exhaustive Search)

### 무식하게 다해보기(Brute-force)

- 모든 경우의 수를 탐색

```python
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
# range 범위 주의!!
```

### 델타 탐색(Delta Search)

- 이차원 리스트에서 상하좌우 탐색
- 행과 열의 변량인 -1, +1을 델타(delta)값 이라 함
  ![image](https://user-images.githubusercontent.com/110805149/216060505-d956d83a-9670-4b62-a020-c567a038f29f.png)

```python
x = 1
y = 1
# 행을 x 열을 y로 표현(또는 행을 r 열을 c)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# # 상
# nx = x + dx[0]
# ny = y + dy[0]
# # 하
# nx = x + dx[1]
# ny = y + dy[1]
# # 좌
# nx = x + dx[2]
# ny = y + dy[2]
# # 우
# nx = x + dx[3]
# ny = y + dy[3]

# for i in range(4):
#     nx = x + dx[i]
#     ny = y + dy[i]

# 상하좌우 튜플로도 가능

# 이동 후 범위 확인, 끝 부분, 엣지 확인
for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    # 범위 안에 있으면 갱신하기(3*3 행렬 기준)
    if 0 <= nx < 3 and 0 <= ny < 3:
        x = nx
        y = ny
```

## 참고

- reversed(range(m)): range를 역으로
- zip으로 회전, 전치하기

```python
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 0, 1, 2]
]
#
transpose = [[0]*3 for i in range(4)]
print(transpose)

for x in range(3):
    for y in range(4):
        transpose[y][x] = matrix[x][y]

print(transpose)
```

# 알고리즘 10일차

## 그래프(Gragh)

- 정점(Vertex)과 이를 연결하는 간선(Edge)들의 집합으로 이루어진 비선형 자료구조

### 그래프 용어

- 정점(Vertex): 간선으로 연결되는 객체, 노드(Node)라고도 함
- 간선(Edge): 정점 간의 관계(연결)를 표현하는 선
- 경로(Path): 시작 정점부터 도착 정점까지 거치는 정점을 나열한 것
- 인접(Adjacency): 두 개의 정점이 하나의 간선으로 직접 연결된 상태
- 차수(Degree): 하나의 정점에 연결된 간선의 개수

### 그래프의 종류

- 무방향 그래프(Undirected graph)

  - 간선의 방향이 없음
  - 모든 정점의 차수의 합 = 간선 수 x 2

- 유방향 그래프(Directed graph)
  - 간선의 방향이 있음
  - 진입 차수(들어오는 간선)와 진출 차수(나가는 간선)로 나뉨

### 그래프의 표현

- 인접행렬(Adjacent matrix)

  - 두 정점 연결하는 간선 없으면 0, 있으면 1을 가지는 행렬로 표현
    ![image](https://user-images.githubusercontent.com/110805149/216334824-959f7a73-14dd-4094-aba9-34dabe4a5014.png)

- 인접리스트(Adjacent list)

  - 리스트를 통해 각 정점에 대한 인접 정점들을 순차적으로 표현
  - 인접리스트의 길이 자체가 간선 수
    ![image](https://user-images.githubusercontent.com/110805149/216335221-41050429-c54c-4750-b8a7-5b12c193a305.png)

- 인접 행렬은 직관적이고 만들기 편하지만 공간 낭비 가능
- 인접리스트는 효율적
- ex.정점 100개 , 간선 5개 -> 인접리스트 쓰면 좋음
- ex.정점 8개 간선 50개 -> 인접행렬 쓰는게 나음

## 참고

- itertools(순열조합 라이브러리):순열, 조합, 중복순열, 중복조합 등

# 알고리즘 11일차

## 깊이 우선 탐색(DFS)

- 그래프 탐색 알고리즘이란?
  - 시작 정점에서 간선을 타고 이동할 수 있는 모든 정점을 찾는 알고리즘
- 그래프 탐색 알고리즘에는 깊이우선탐색과 너비 우선 탐색이 있다.
- 탐색은 모든 케이스에 적용 가능해야 함

### 깊이 우선 탐색(Depth-First Search, DFS)

- 그래프의 깊이를 우선 탐색하기 위해 `스택` 활용

### 너비우선 탐색(Breadth_First Search, BFS)

- 그래프의 너비를 우선 탐색하기 위해 `큐` 활용

### 깊이 우선 탐색의 특징

- 갈 수 있는 하위 정점까지 가장 깊게 탐색
- ex. 미로 탈출(막히면 다시 돌아와서 다른길 탐색)
- 모든 정점을 방문할 때 유리, 따라서 경우의 수, 순열조합에서 많이 사용
- 너비우선탐색(BFS)에 비해 코드 구현 간단함
- 단, 모든 정점을 방문할 필요가 없거나 최단 거리를 구하는 경우 너비우선탐색(BFS) 유리

### DFS 동작 과정

- 탐색을 진행할 그래프(인접행렬, 인접리스트) 필요
- `각 정점 방문 여부 판별` 체크리스트
- DFS 사이클
  1. 정점 방문처리 및 스택
  2. 스택 마지막 값 꺼내고 인접한 정점 확인
  3. 방문하지 않은 인접 정점 -> 1번

### DFS 구현 방식

- 직전 방문 정점으로 돌아가야 하므로 후입선출의 스택 사용

1. visited = [False]로 방문한 곳 체크 하기
2. stack 사용해서 최근 방문 경로 확인

```python
# network: 탐색을 진행할 그래프
def dfs(start)
    visited = [False]*(n+1) # 방문처리 리스트 만들기
    stack = [start] # 돌아갈 곳 기록
    visited[start] = True # 시작 정점 방문 처리

    while stack: # 스택이 빌 때까지(돌아갈 곳 없을 때까지) 반복
        cur = stack.pop() # 현재 방문 정점(후입선출)
        for i in network[cur]: # 인접한 모든 정점에 대해
            if not visited[i]:  # False면 실행(아직 방문 안했으면)
                visited[i] = True # 방문처리
                stack.append(i) # 스택에 넣기

dfs(0) # 0번 정점에서 시작
```

## 참고

- 인접리스트 0번 없으면 그냥 비워두는게 좋음(ex. [[],[1]})
