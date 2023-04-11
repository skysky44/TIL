from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    comment_form = CommentForm()
    article = Article.objects.get(pk=pk)
    # 해당 게시글에 작성된 모든 댓글을 조회(역참조)
    comments = article.comment_set.all()

    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    article.delete()

    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        comment = comment_form.save(commit=False) # 커밋 잠시 멈춤
        # 인스턴스는 만들어주는데 DB에 저장은 안함

        comment.article = article  # 인스턴스 채우고 잠시 저장 미뤘다가 id 채우고 저장하기
        comment.save()
        # True가 기본값
        

        return redirect('articles:detail', article_pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk 도 가능
    # 댓글 삭제
    comment.delete()
    return redirect('articles:detail', article_pk)


# article = Article()
# article.title = 'aaa'
# article.content = 'sadasd'
# article.save()

# comment = Comment()
# comment.content = '댓글 내용'
# comment.save() # ??/

# In [7]: comment.content
# Out[7]: 'first comment'

# In [8]: comment.article
# Out[8]: <Article: Article object (1)>

# In [9]: comment.article.title
# Out[9]: '제목'

# In [10]: comment.article.pk
# Out[10]: 1
