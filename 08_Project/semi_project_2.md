# 프로젝트에서 새로 알게 된 내용 또는 후기


# 230509
- 기본 뷰 피그마, 피그잼 작성

# 230510
- 다 같이 자세하게 모델 작성(추후 작업 시 용이)

- 쿼리 파라미터: ? 카테고리 필터 적용(url에 변수 사용 안하고)
```html
<div>
    <a href="{% url 'communities:comment_index' %}">All</a>
    <a href="{% url 'communities:comment_index' %}?category=qna">Q&A</a>
    <a href="{% url 'communities:comment_index' %}?category=worry">Worry</a>
    <a href="{% url 'communities:comment_index' %}?category=study">Study</a>
    <a href="{% url 'communities:comment_index' %}?category=etc">Etc</a>
</div>


{% if category %}
    <h2>Category: {{ category }}</h2>
{% else %}
    <h2>All Categories</h2>
{% endif %}


{% for comment in comments %}

{% endfor %}
```

```python
def comment(request):
    comments = Comment.objects.all()
    category = request.GET.get('category', None)
    comments = Comment.objects.all()

    if category:
        comments = comments.filter(category=category)

    context = {
        'comments': comments,
        'category': category,
    }

    return render(request, 'communities/comment_index.html', context)

```

## 230519
- 회고
- keep
- 팀원들의 열정!
- 시작부터 팀원 모두가 미리 모델 설계를 신중하게 했던 부분이 초반 작업 속도를 향상 시켜주었습니다. 물론 그 시간이 힘들게 느껴 질 수는 있겠지만 분명 중요한 부분이고 추후에 조금씩 변화를 주기에도 용이했습니다.
- 피그잼 활용해서 view를 설계한 부분도 시간을 충분히 사용해서 빠른 진행을 할 수 있었던 것 같습니다.


- problem
- 백으로 결정하고 시작했지만 프론트를 안 하다가 해보고 싶어서 도전 했는데 어려웠습니다. 진행 속도가 떨어지다 보니 조금 어려웠습니다. 그래서 기본적 구현 위주로 구현 하게 되었고 그러다 보니 다양한 기능을 적용해보진 못해서 아쉬움이 남습니다. 물론 오랜만에 프론트를 하면서 복습도하고 이해도 많이 해서 좋았습니다.

- try
- 다음주에는 클론을 넘어서서 조금 더 여유를 갖고 부가적인 기능들을 더 적용해볼 수 있으면 좋을 것 같아요. 일주일 정도가 너무 빨리 지나갔습니다. 건강 관리 + 목표 달성