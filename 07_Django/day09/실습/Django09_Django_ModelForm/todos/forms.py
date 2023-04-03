from .models import Todo
from django import forms


class TodoForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '제목 입력'
            },
        )
    )
    content = forms.CharField(
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': '내용 입력'
            },
        ),
    )
    priority = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'min': 1, 'max': 5, 'value': 3
            },
        ),
    )
    deadline = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date'
            },
        ),
    )

    class Meta:
        model = Todo
        fields = '__all__'
