from django import forms
from .models import Post, Comment, FreePost, FreeComment
# django의 forms를 가져온다

class PostForm(forms.ModelForm):
   class Meta:
        model = Post # Post라는 model을 기반으로 만들어준다
        fields = '__all__' # 전체필드 추가 
        # fields = ['title', 'body']  #특정값만 받고 싶다면 이렇게
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)

            self.fields['title'].widget.attrs = {
                'class': 'form-control',
                'placeholder': "글 제목을을 입력해주세요",
                'rows': 20
            }

            self.fields['body'].widget.attrs = {
                'class': 'form-control',
                'placeholder': "글 제목을을 입력해주세요",
                'rows': 20,
                'cols' : 100
            }

class CommentForm(forms.ModelForm): # 댓글을 입력할 수 있는 form 
   class Meta:
        model = Comment # Post라는 model을 기반으로 만들어준다
        fields = ['comment'] #  댓글 

        def __init__(self, *args, **kwargs):
            super(CommentForm, self).__init__(*args, **kwargs)


class FreePostForm(forms.ModelForm):
       class Meta:
        model = FreePost # Post라는 model을 기반으로 만들어준다
        fields = ['title', 'body']  #특정값만 받고 싶다면 이렇게

        def __init__(self, *args, **kwargs):
            super(FreePostForm, self).__init__(*args, **kwargs)

            self.fields['title'].widget.attrs = {
                'class': 'form-control',
                'placeholder': "글 제목을을 입력해주세요",
                'rows': 20
            }

            self.fields['body'].widget.attrs = {
                'class': 'form-control',
                'placeholder': "글 제목을을 입력해주세요",
                'rows': 20,
                'cols' : 100
            }



class FreeCommentForm(forms.ModelForm): # 댓글을 입력할 수 있는 form 
   class Meta:
        model = FreeComment # Post라는 model을 기반으로 만들어준다
        fields = ['comment'] #  댓글 
    
        def __init__(self, *args, **kwargs):
            super(FreeCommentForm, self).__init__(*args, **kwargs)
    
            self.fields['comment'].widget.attrs = {
                'class': 'form-control',
                'placeholder': "댓글을 입력해주세요",
                'rows': 10
            }
