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
            article = form.save(commit=False)
            article.user = request.user
            # article의 user필드에 request의 user 저장
            article.save()
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
    if request.user == article.user: #본인만 삭제 가능
        article.delete()

    return redirect('articles:index')


# 수정은 작성자가 안바뀌어서 수정 코드 필요 없다.
# 그냥 두면 아무나 수정 가능
# 현재 수정을 진행 하려는 유저 vs 글 작성자 비교


@login_required # 막는거 뿐만 아니라 로그인 페이지로 리다이렉트
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
    # 현재 수정을 진행 하려는 유저 vs 글 작성자 비교
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

@login_required
def comment_create(request, article_pk):
    # 몇 번 게시글인지 조회
    article = Article.objects.get(pk=article_pk)
    # 댓글 데이터를 받아서
    comment_form = CommentForm(request.POST)
    # 유효성 검증
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user # 유저 추가
        comment.save()

        

        return redirect('articles:detail', article_pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comment_delete(request, article_pk, comment_pk):
    # 삭제할 댓글을 조회
    comment = Comment.objects.get(pk=comment_pk)
    # article_pk = comment.article.pk 도 가능
    
    # 댓글 삭제를 요청하는자 vs 댓글 작성자 
    if request.user == comment.user: 
        # 댓글 삭제
        comment.delete()
    return redirect('articles:detail', article_pk)

