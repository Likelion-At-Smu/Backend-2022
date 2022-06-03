from django import forms
from .models import Post, Comment, FreePost, FreeComment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # 특정 field만 받고 싶을 때는
        # fields = ['title', 'body']

    # bootstrap 클래스 사용하려면 widget 사용
    # def __init__(self, *args, **kwargs):
        # super(PostForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs = {
        #   'class': 어쩌구,
        #   'placeholder': "글 제목을 입력해주세요",
        #   'rows': 20
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body']

class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']