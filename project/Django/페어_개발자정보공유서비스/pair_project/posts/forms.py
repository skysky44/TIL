from .models import Post
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    CHOICES = [
        ('개발', '개발'),
        ('CS', 'CS'),
        ('신기술', '신기술'),
        ('진짜신기술', '진짜신기술'),
    ]
    category = forms.ChoiceField(
        widget=forms.Select,
        choices=CHOICES
    )

    class Meta:
        model = Post
        fields = '__all__'