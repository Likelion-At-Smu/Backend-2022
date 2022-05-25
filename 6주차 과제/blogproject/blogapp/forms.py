# django form을 담을 수 있는 파일
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField(widget = forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__' #: 모든 값 입력받기

        #특정값만 입력받기
        #fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
    

        #특정값만 입력받기
        fields = ['comment']