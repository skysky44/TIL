from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model




# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('reviews:index')

    else:
        form = CustomUserCreationForm()

    context = {
        'form' : form 
    }
    
    return render(request, 'accounts/signup.html', context)



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('reviews:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)




def logout(request):
    auth_logout(request)
    return redirect('reviews:index')



def profile(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)
    context = {
        'user' : user,
    }
    return render(request, 'accounts/profile.html', context)