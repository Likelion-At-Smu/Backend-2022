from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    # 블로그 글들을 띄우는 코드
    posts = Blog.objects.all()
    # posts = Blog.objects.filter().order_by('-date')
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        # 객체 생성
        post = Blog()
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # 객체 저장
        post.save()
    return redirect('home')

# django form을 이용해서 입력값 받는 함수
# GET 요청과 (= 입력값을 받는 html을 갖다 줘)
# POST 요청 (= 입력한 내용을 데이터 베이스에 저장. form에서 입력한 내용을 처리)
# 둘 다 처리가 가능함
def formcreate(request):
    if (request.method == 'POST'):
        form =  BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title'] 
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
    # 세 번째 인자로 데이터 넘기기 가능. 딕셔너리 형태
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form =  BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

# blog_id(pk 값)도 같이 인자로 받음
def detail(request, blog_id):
    # get_object_or_404 : 특정 pk 값을 갖고 있는 특정 모델 객체만 가져올 때 사용
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail':blog_detail, 'comment_form':comment_form})

def create_comment(request, blog_id):
    filed_form = CommentForm(request.POST)

    if filed_form.is_valid():
        # 어떤 게시물의 댓글인지 같이 저장해줘야 함
        finished_form = filed_form.save(commit=False)
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()

    return redirect('detail', blog_id)
