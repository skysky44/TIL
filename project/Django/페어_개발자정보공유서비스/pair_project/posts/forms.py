from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    CHOICES = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술'),
    ]
    category = forms.ChoiceField(
        widget=forms.Select,
        choices=CHOICES
    )

    class Meta:
        model = Post
        fields = '__all__'