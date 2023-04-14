from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디 입력',
                'style': 'width: 350px',
            })
    )
    first_name = forms.CharField(
        label='이름',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이름 입력',
                'style': 'width: 350px',
            })
    )
    last_name = forms.CharField(
        label='성',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '성 입력',
                'style': 'width: 350px',
            })
    )

    email = forms.EmailField(
        label='이메일',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '이메일 입력',
                'style': 'width: 350px',
            })
    )

    password1 = forms.CharField(
        label='비밀번호',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 입력',
                'style': 'width: 350px',
            })
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 재입력',
                'style': 'width: 350px',
            })
    )


    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '아이디 입력',
                'style': 'width: 350px',
            })
    )

    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': '비밀번호 입력',
                'style': 'width: 350px',
            })
    )

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password')

