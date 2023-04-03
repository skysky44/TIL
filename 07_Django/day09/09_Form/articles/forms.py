from django import forms
from .models import Article

# 일반 Form
# class ArticledForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

# ModelForm


class ArticledForm(forms.ModelForm):
    # 클래스 안에 클래스? Inner class 파이썬 문법이랑 아무상관 없고
    # 그냥 django ModelForm의 구조가 이렇게 설계 되었을 뿐
    # 그냥 modelform에 대한 추가 정보를 클래스 meta에 쓸 뿐
    # form에 대한 추가 데이터(meta) 라고 생각하면 됨

    # 위젯으로 input 디자인 변경. class 추가 하기.공식문서확인.
    title = forms.CharField(
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': '제목을 입력해주세요.'
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용을 입력해주세요',
                'rows': 5,
                'cols': 50,
            }
        ),
        error_messages={'required': '내용을 입력하세요.'},
    )

    # ModelForm의 정보를 작성 하는 곳

    class Meta:
        model = Article
        fields = '__all__'
        # fields = ('content',)
        # content만 출력
        # exclude = ('title',)
        # title 제외하고 출력
