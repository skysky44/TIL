"""
1. 아래 할 일 생성
content : 실습 제출
priority : 5
completed : False
deadline : 오늘 날짜(년-월-일)
"""
todo = Todo()

todo.content = '실습 제출'

todo.priority = 5

todo.completed = False

todo.deadline = '2023-03-28'

todo.save()

"""
2. 아래 할 일 생성
content : 데일리 설문(오후) 제출
deadline : 오늘 날짜(년-월-일)
"""
todo = Todo(content='데일리 설문(오후) 제출', deadline='2023-03-28')

todo.save()

"""
3. 임의의 할 일 5개 생성
"""
Todo.objects.create(content='class 복습', deadline='2023-03-28')
Todo.objects.create(content='알고리즘 풀기', deadline='2023-03-28')
Todo.objects.create(content='강의 복습', deadline='2023-03-28')
Todo.objects.create(content='저녁 먹기', deadline='2023-03-28')
Todo.objects.create(content='휴식', deadline='2023-03-28')

"""
4. pk 기준 오름차순으로 정렬한 모든 데이터 조회
"""

Todo.objects.order_by('pk')

"""
5. priority 기준 내림차순으로 정렬한 모든 데이터 조회
"""
Todo.objects.order_by('-priority')


"""
6. pk가 1인 단일 데이터의 아래 필드 조회
(pk, content, priority, deadline, created_at)
"""
data = Todo.objects.get(pk=1)
data.pk
data.content
data.priority
data.deadline
data.created_at
