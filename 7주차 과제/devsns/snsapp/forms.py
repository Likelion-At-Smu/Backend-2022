#model form을 기반으로 하는 입력 방식
from django import forms
from .models import Post, Comment, FreePost, FreeComment

# 입력 공간을 만들어줄 form
class PostForm(forms.ModelForm):
    
    class Meta:
        # post라는 모델을 기반으로 form을 생성한다.
        model = Post
        # field 전체를 입력받는다.
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        # 부트스트랩의 클래스를 사용하기 위한 부분
        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }

#댓글 입력 form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # 직접 입력하는 부분은 댓글의 내용
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

class FreePostForm(forms.ModelForm):
    class Meta:
        model = FreePost
        fields = ['title', 'body']

    def __init__(self, *args, **kwargs):
        super(FreePostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20,
            'cols' : 100
        }


class FreeCommentForm(forms.ModelForm):
    class Meta:
        model = FreeComment
        fields = ['comment']

    def __init__(self, *args, **kwargs):
        super(FreeCommentForm, self).__init__(*args, **kwargs)

        self.fields['comment'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }