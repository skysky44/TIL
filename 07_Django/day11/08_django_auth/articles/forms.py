from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article  # 어떤 모델을 등록할지?
        fields = '__all__'


# class UserCreationForm(forms.ModelForm):
#     class Meta:
#         model = User #여기가 auth.user에 연결되어있음..
