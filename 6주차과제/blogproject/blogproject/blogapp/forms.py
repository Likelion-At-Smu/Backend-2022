# form을 정의할 수 있는 py파일을 app파일에 만들었음 ! 
from django import forms
from .models import Blog, Comment

class BlogForm(forms.Form) :
    # 내가 입력받고자하는 값들
    title = forms.CharField()
    body = forms.CharField(widget=forms.Textarea)

class BlogModelForm(forms.ModelForm) :
    class Meta :
        model = Blog
        # fields = ['title','body'] 
        fields = '__all__' # 전체 데이터 

# django form vs. django modelform 
# django form 
# 우리가 입력 받고자하는 값들을 form에다쓰고 views.py에서 실시간으로 객체 생성(post = Blog())
# 객체 안에 입력된 값 저장 

# django modelform 
# form 자체가 model을 기반으로 만들어짐 -> 간편하게 form 형성 가능, form자체적으로 save()함수 값은 것을 가지고 있음

class CommentForm(forms.ModelForm) :
     class Meta :
        model = Comment
        fields = ['comment']
