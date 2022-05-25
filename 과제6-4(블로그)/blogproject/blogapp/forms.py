#django에서 기본적으로 제공하고 있는 form 기능들을 여기에다 구현할 것이다
from django import forms
from .models import Blog, Comment

#=========@@@@@_1. django가 일반적으로 제공하는 form 과 @@=============

class BlogForm(forms.Form): # django에서 가져온  forms에서 Form을 상속받는다
    # 내가 입력받고자 하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)


#========@@@@_2  model을 기반으로 만들 수 있는 form @@===============

class BlogModelForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'  
      #Blog 안의 모든 값을 받고 싶으면 언더바(_)2번씩 앞뒤로
      # fields =['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']