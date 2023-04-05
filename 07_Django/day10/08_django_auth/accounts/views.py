from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
# 로그인 폼 import
from django.contrib.auth import login as auth_login  # login 이름이 겹쳐서 수정
from django.contrib.auth import logout as auth_logout
# Create your views here.
# 1. 로그인 페이지(GET)
# 2. 로그인 실행 로직(POST)


def login(request):
    if request.method == 'POST':
        # 첫번째인자 request. modelform이랑 형태 다름
        form = AuthenticationForm(request, request.POST)
        if form.is_valid:
            # 첫번째인자 request 두번째는 인증된 유저 필요
            # AuthenticationForm(request.POST)에 .get_user하면 인증된 유저 나옴
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


# 로그아웃: 세션을 삭제함
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
