from django import forms
from .models import Review, Comment


class ReviewForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '제목 입력',
                'style': 'width: 350px',
            })
    )
    content = forms.CharField(
        label='내용',
        label_suffix='',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': '내용 입력',
                'style': 'width: 350px',
            })
    )
    movie = forms.CharField(
        label='영화',
        label_suffix='',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '영화제목 입력',
                'style': 'width: 350px',
            })
    )


    
    class Meta:
        model = Review
        fields = ('title', 'content', 'movie', 'image')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs={
                'class': 'form-control input-group',
                'placeholder' : ' 댓글을 입력해주세요'
            }
        
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)
