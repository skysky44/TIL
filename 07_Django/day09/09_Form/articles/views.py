from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticledForm


# Create your views here.


def index(request):

    articles = Article.objects.all()

    context = {
        'articles': articles
    }

    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


# def new(request):
#     form = ArticledForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     # title = request.POST.get('title')
#     # content = request.POST.get('content')
#     # article = Article(title=title, content=content)
#     # article.save()

#     form = ArticledForm(request.POST)
#     if form.is_valid():
#         # is_valid True가 아니면 form에 통과 못한 정보를 담아 내려줌
#         article = form.save()
#         return redirect("articles:detail", article.pk)
#     # 에러메시지 전달 위해 context
#     context = {
#         'form': form,
#     }
#     # 에러메시지 보려고 render context 사용
#     return render(request, 'articles/new.html', context)


def create(request):
    # HTTP requests method POST라면
    if request.method == 'POST':
        form = ArticledForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
        # context = {
        #     'form': form,
        # }
        # return render(request, 'articles/new.html', context)
    # POST가 아니라면
    else:
        form = ArticledForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/new.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)

    article.delete()

    return redirect('articles:index')


# def edit(request, pk):
#     article = Article.objects.get(pk=pk)

#     form = ArticledForm(instance=article)
#     # 기존 내용 불러오기 위해 instance= 입력

#     context = {
#         'article': article,
#         'form': form,
#     }

#     return render(request, 'articles/edit.html', context)


# def update(request, pk):

#     # article = Article.objects.get(pk=pk)
#     # article.title = request.POST.get('title')
#     # article.content = request.POST.get('content')
#     # article.save()

#     article = Article.objects.get(pk=pk)
#     form = ArticledForm(request.POST, instance=article)
#     # save가 instance=article로 수정 또는 생성을 판단 함
#     # new와 update 차이는 instance=article
#     # data=request.POST에서 순서상 data가 생략 되어있는 것임
#     if form.is_valid():
#         article = form.save()
#         return redirect("articles:detail", article.pk)
#     context = {
#         'article': article,
#         'form': form,
#     }
#     return render(request, 'articles/edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticledForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect("articles:detail", article.pk)
    else:
        form = ArticledForm(instance=article)

    context = {
        'article': article,
        'form': form,
    }

    return render(request, 'articles/edit.html', context)
