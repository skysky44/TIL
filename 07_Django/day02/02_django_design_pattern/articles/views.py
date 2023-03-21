from django.shortcuts import render
# render 페이지를 만들어주는 함수


# Create your views here.
# 특정 기능을 수행하는 view 함수를 만듦
def index(request):
    return render(request, 'articles/index.html')
# return 응답(메인페이지)
#  'index.html'안에는 경로가 들어가야함 articles/index.html
