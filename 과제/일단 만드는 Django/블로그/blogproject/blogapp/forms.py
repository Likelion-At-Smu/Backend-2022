from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form):
    # 내가 입력받고자 하는 값
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

# Model을 기반으로 form이 만들어져서 좀 더 수월한 편
class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        # 전체를 입력받고 싶을 때
        fields = '__all__'
        # 일부 -> fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']