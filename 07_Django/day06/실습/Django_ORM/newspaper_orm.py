"""
1. pk 필드가 1인 단일 데이터의 journalist 필드 조회
답 : Laney Mccullough
"""
Newspaper.objects.get(pk=1).journalist


"""
2. journalist 필드가 Laney Mccullough인 데이터 개수 조회
답 : 858
"""

Newspaper.objects.filter(journalist='Laney Mccullough').count()

"""
3. pk 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (10000)>, <Newspaper: Newspaper object (9999)>, ...생략
"""
Newspaper.objects.order_by('-pk')

"""
4. created_at 필드 기준 내림차순으로 정렬한 모든 데이터 조회
답 : <QuerySet [<Newspaper: Newspaper object (4719)>, <Newspaper: Newspaper object (97)>, ...생략
"""

Newspaper.objects.order_by('-created_at')

"""
5. journalist 필드가 Britney를 포함하는 데이터 개수 조회
답 : 799
"""

Newspaper.objects.filter(journalist__contains='Britney').count()

"""
6. journalist 필드가 ['Britney Mahoney', 'Arianna Walls', 'Carl Short']에 속하는 데이터 개수 조회
답 : 2469
"""
Newspaper.objects.filter(
    journalist__in=['Britney Mahoney', 'Arianna Walls', 'Carl Short']).count()

"""
7. created_at 필드가 2000-01-01 이후 데이터 개수 조회
답 : 4355
"""
Newspaper.objects.filter(created_at__gt='2000-01-01 00:00:00').count()


"""
8. 마지막 단일 데이터의 title, content, journalist 필드를 조회하고 아래와 같은 형식으로 출력
답
title : Teach father within million consumer baby its.
content : Then member effort want site. Radio represent yard bag fine. Congress movie ten along.
Hand receive agree science present main. Other member every.
journalist : Laney Mccullough
"""
paper = Newspaper.objects.latest('pk')

print(f'title : {paper.title}')
print(f'content : {paper.content}')
print(f'journalist : {paper.journalist}')


"""
기타 ORM 코드 작성 후 해당 코드와 결과 코드 리뷰 시간에 공유
"""
