from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields='__all__' # fields = '__all__' 라고하면 models.py의 Blog안에 있는 모든 데이터 
        # fields = ['title', 'body'] 는 Blog안에 tilte, body만

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']