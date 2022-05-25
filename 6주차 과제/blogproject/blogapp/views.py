from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm
# Create your views here.

def home(request):
    #블로그 객체들을 출력하는 코드

    #저장된 블로그 객체들을 모두 가져오기
    posts = Blog.objects.all()
    #원하는 순서, 값 을 지정하기
    #-는 내림차순
    Blog.objects.filter().order_by('date')
    return render(request, 'index.html',{'posts':posts})

# 블로그를 작성하는 함수
def new(request):
    return render(request, 'new.html')
#블로그를 저장하는 함수
def create(request):
    if(request=='POST'):
        #blog 객체 생성
        post = Blog()
        #입력받은 값 저장
        post.title = request.POST['title']
        post.body = request.POST['body']
        #현재시각 저장
        post.date = timezone.now()
        #저장
        post.save()

    #저장이 끝나면 home으로 돌아가라
    return redirect('home')

#get요청과 post요청을 하나의 url에서 동시에 처리할 수 있다.
def formcreate(request):
    if request.method=='POST':
        form = BlogForm(request.POST)
        # form 값의 유효성 검사
        if form.is_valid():
            #blog 객체 생성
            post = Blog()
        #입력받은 값 저장
        #유효한 값이라고 표시
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
        #현재시각 저장
            post.date = timezone.now()
        #저장
            post.save()
            return redirect('home')
    else:#get요청
        form = BlogForm()
    return render(request, 'formcreate.html', {'form':form})

def modelformcreate(request): 
    if request.method=='POST'or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES)
        # form 값의 유효성 검사
        if form.is_valid():
            #이미 형식에 맞게 저장되어 있기 때문에 바로 저장 가능
            form.save()
            return redirect('home')
    else:#get요청
        form = BlogModelForm()
    #같은 파일을 사용해도 상관없다.
    return render(request, 'formcreate.html', {'form':form})

#pk값을 매개변수로 받는다
def detail(request, blog_id):
    #blog_id를 pk로 사용하여 blog값을 가져오고 만약 실패하면 404error를 발생시켜라
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'blog_detail':blog_detail,'comment_form':comment_form})

#댓글을 저장하는 함수
def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    #filled_form이 유효하다면 저장해라
    if filled_form.is_valid():
        #아직 저장하지 않고 대기
        finished_form = filled_form.save(commit=False)
        #어떤 게시물에 대한 댓글인지 post에 저장해라
        finished_form.post = get_object_or_404(Blog, pk = blog_id)
        #저장
        finished_form.save()
    
    return redirect('detail',blog_id)