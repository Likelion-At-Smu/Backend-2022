from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['title', 'body'] title과 body만 가져올 때

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']