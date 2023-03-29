from django.shortcuts import render
from .models import Article


# Create your views here.


def index(request):
    # DB에 전체 게시글 조회를 요청
    articles = Article.objects.all()  # 전체 조회니까 복수형 articles로 변수
    # print(articles)
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    # print(article)
    context = {
        'article': article,  # 단일객체 조회라서 단수형으로
    }
    return render(request, 'articles/detail.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    # new에서 보낸 사용자 데이터를 받아서 변수에 할당
    # print(request.GET)
    title = request.GET.get('title')
    content = request.GET.get('content')
    # request.GET 데이터 dictionary다

    # # 받은 데이터를 DB에 저장
    # # 1
    # article = Article()
    # article.title = title
    # article.content = content
    # article.save()

    # 2 (2번을 사용하기로)
    article = Article(title=title, content=content)
    # 저장 전에 유효성 검사와 같은 추가 작업을 위해 2번 방법 택함(현재는 models.py에 있는 max_length 동작 안하고 있음..)
    article.save()

    # 3
    # Article.objects.create(title=title, content=content)

    # 결과 페이지 반환
    return render(request, 'articles/create.html')
