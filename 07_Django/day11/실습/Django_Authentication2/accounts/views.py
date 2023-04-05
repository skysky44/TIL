from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm, UserChangeForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    form = AuthenticationForm(request)
    context = {
        'form': form
    }

    return render(request, 'accounts/index.html', context)


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 확인: 가입 후 로그인
            return redirect('accounts:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            # 막힘 form.get_user()
            return redirect('accounts:index')
    else:
        form = AuthenticationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):

    auth_logout(request)

    return redirect('accounts:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user) # 확인
        if form.is_valid():
            form.save()
            
            return redirect('accounts:index')

    else:
        form = CustomUserChangeForm(instance=request.user)

    context = {
        'form':form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # 확인  request.POST
        if form.is_valid():
            user = form.save()
            # 확인 로그인 유지하기
            update_session_auth_hash(request, user)
            return redirect('accounts:index')
        pass
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form':form
    }
    return render(request, 'accounts/change_password.html', context)


@login_required
def delete(request):
    request.user.delete() # 확인. 기억안남
    return redirect('accounts:index')