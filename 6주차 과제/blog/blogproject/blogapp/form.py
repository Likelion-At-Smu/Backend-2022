from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form) :
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # 모든 필드를 입력받고 싶을 때
        fields = '__all__'
        # 특정 필드만 입력받고 싶을 때
        #fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']