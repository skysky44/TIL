# from django.shortcuts import render (이제 필요 없음)
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

# Create your views here.
# drf는 api view 데코레이터 필수임
# 4. 해당 view 함수가 어떤 http 요청 메서드를 허용하는지 결정하는 데코레이터 작성(drf의 view함수에서 필수)
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 1. 제공할 게시글 목록 조회
        articles = Article.objects.all()

        # 2. 게시글 목록 데이터를 직렬화(serialization)
        serializer = ArticleListSerializer(articles, many=True) #many 앞의 데이터가 다중데이터(쿼리셋: 객체모음)일때 True로 단일일 때 false

        # 3. 직렬화된 데이터를 json 데이터로 응답
        return Response(serializer.data) 
            #.data 그냥 문법임

    elif request.method == 'POST':
        # 사용자 데이터를 받아서 serializer로 직렬화
        serializer = ArticleSerializer(data=request.data)
        # request.post였는데 drf에서는 request.data
        # 유효성 검사
        if serializer.is_valid():
            # drf가 장고개발자위해 똑같이 is_valid만들어둠
            serializer.save()
            # 생성 성공 시 201 응답
            # 원래는 성공 시 status 200이 기본값인데 정확히는 201이 맞음
            return Response(status=status.HTTP_201_CREATED)
        # 생성 실패 시 400 응답
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        # 단일데이터 many 없어도 됨
        return Response(serializer.data)

    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # 삭제 성공 204

    elif request.method == 'PUT':
        # 사용자 데이터를 받아서 serializer로 직렬화 + 기존 데이터
        serializer = ArticleSerializer(article, data=request.data)
        # 앞이 instance 뒤에 객체
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
            # 수정은 생성의 하나로 봐서 status 따로 없음. 규약에 맞춰 쓰는 것뿐
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) - 생략 가능(is_valid(raise_exception=True) 대체)


@api_view(['GET'])
def comment_list(request):
    comments = Comment.objects.all()
    serializer = CommentSerializer(comments, many= True)
    return Response(serializer.data)
        # drf에서 .data는 json 데이터로 만들어줌

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)




@api_view(['POST'])
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        # 과거의 commit=False랑 동일한 article=article
        return Response(serializer.data, status=status.HTTP_201_CREATED)