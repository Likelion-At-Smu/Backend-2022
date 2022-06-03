# get_object_or_404: pk 값을 이용해 특정 모델 객체 하나만 가져옴 !
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request):
    # 블로그 글을 전부 띄우는 코드
    # posts = Blog.objects.all()
    posts = Blog.objects.filter().order_by('date')
    return render(request, 'index.html', {'posts':posts})

# 블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html')

# 블로그 글을 저장해주는 함수
def create(request):
    # request의 method가 POST라면
    if(request.method == 'POST'):
        post = Blog() # post 변수에 Blog 객체 생성
        # POST 요청 안에 있는 데이터를 담아줌
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        # 모델 객체를 DB에 저장
        post.save()
    # 정상적으로 종료되면 home으로 다시 돌아가도록 함
    return redirect('home')

# django form을 이용해서 입력값을 받는 함수
# GET(입력값을 받을 수 있는 html을 줘야 함)
# POST 요청(입력한 내용을 DB에 젖아, form에서 입력한 내용을 처리)
# GET과 POST 모두 처리 가능
def formcreate(request):
    if request.method == 'POST':
        # 입력 내용을 DB에 저장
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')

    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogForm()
    
    # render 인자로 views.py 데이터를 html에 *딕셔너리*로 전달 가능
    return render(request, 'form_create.html', {'form':form})

def modelformcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        # 입력을 받을 수 있는 html 갖다주기
        form = BlogModelForm()
    
    # render 인자로 views.py 데이터를 html에 *딕셔너리*로 전달 가능
    return render(request, 'form_create.html', {'form':form})

def detail(request, blog_id):
    # blog_id 번째 블로그 글을 DB로 부터 가져와
    # 블로그 객체 중 pk가 blog_id인 것을 가져옴,,
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    
    comment_form = CommentForm()

    # blog_id 번째 글을  detail.html에 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail':blog_detail}, {'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        # filled form을 저장하지 않고 대기
        finished_form = filled_form.save(commit=False)
        # 블로그 객체 중 pk가 blog_id인 것만 가져옴
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        finished_form.save()
    
    return redirect('detail', blog_id)