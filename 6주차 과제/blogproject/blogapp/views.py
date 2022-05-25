from django.shortcuts import redirect, render, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommnetForm
from django import forms

# Create your views here.
def home(request):
    #블로그 글들을 모조리 띄우는 코드
    posts = Blog.objects.all()#쿼리셋이라는 자료형태로 감싸져서 보내진다
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html',{'posts': posts})

#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

#블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#장고 폼을 이용해서 입력값을 받는 함수
#GET 요청과(=입력값을 받을 수 있는 HTML을 갖다 줘야함.)
#POST 요청을 (= 입력한 내용을 데이터베이스에 저장 .form에서 입력한 내용을 처리)
# 둘 다 처리 가능가 가능한 함수
def formcreate(request):
    if request.method == 'POST':
        #입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            #저장하는 코드
            post = Blog()
            post.title = form.cleaned_data['title'] #직접 저장
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        #GET요청, 입력을 받을 수 있는 HTML을 갖다주면 된다.
        form = BlogForm()
    return render(request, 'form_create.html',{'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':#requset에 따라서 핸들링
        #입력 내용을 DB에 저장
        form = BlogModelForm(request.POST)
        if form.is_valid():
            #저장하는 코드
            form.save()#폼에서 그대로 세이브하는 방식
            return redirect('home')
    else:
        #GET요청, 입력을 받을 수 있는 HTML을 갖다주면 된다.
        form = BlogModelForm()
    return render(request, 'form_create.html',{'form':form})

def detail(request, blog_id):
    #블로그 아이디 번째 글을 데이터베이스로부터 갖고와서
    blog_detail = get_object_or_404(Blog,pk=blog_id)#get_object_or_404 : pk값을 이용해서 특정 모델 객체 하나만 가져오는 함수
    #블로그 아이디 번째 글을 detail.html로 띄우는 코드
    comment_form = comment_form()
    return render(request, 'detail.html',{'blog_detail' :blog_detail, 'comment_form' : comment_form} )

def create_comment(request, blog_id):
    filled_form =CommnetForm(request.POST)

    if filled_form .is_valid():
        finished_form = filled_form.save(commit=False)#아직은 저장안함.
        finished_form.post = get_object_or_404(Blog, pk=blog_id)#어떤 게시글에 달린 댓글인지 저장 필요
        finished_form.save()

    return redirect('detail', blog_id)
