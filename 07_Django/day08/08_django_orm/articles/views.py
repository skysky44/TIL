from django.shortcuts import render, redirect
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
    title = request.POST.get('title')
    content = request.POST.get('content')

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

    # # 결과 페이지 반환
    # return render(request, 'articles/create.html')

    # 8일차 추가 내용 아래부터

    # # 이동할 주소(url)를 사용자에게 응답
    # # 사용자가 index로 향하게 하는 함수(redirect)
    # return redirect("articles:index")

    # 생성한 글의 주소 이동 응답
    # 새로 생성한 글의 pk를 활용
    # 템플릿과 비교 했을 때 띄어쓰기 대신 쉼표 사용한다고 생각하면 됨
    return redirect("articles:detail", article.pk)


def delete(request, pk):
    # 삭제할 데이터 조회
    article = Article.objects.get(pk=pk)

    # 조회한 데이터 삭제(delete)
    article.delete()

    # 전체 조회 페이지 이동
    return redirect('articles:index')


def edit(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article
    }

    return render(request, 'articles/edit.html', context)


def update(request, pk):
    # 수정 작업 과정
    # 1. 데이터 조회
    article = Article.objects.get(pk=pk)

    # 2. 데이터 수정
    # 2-1 사용자가 입력한 form 데이터 저장
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    # 2-2 조회한 데이터(article)필드 값 변경

    # 3. 데이터 저장
    article.save()

    return redirect('articles:detail', article.pk)
