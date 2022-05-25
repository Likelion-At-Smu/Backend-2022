from gc import get_objects
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .form import BlogForm, BlogModelForm, CommentForm

def home(request):
    #Blog DB에 저장되어 있는 글을 모두 띄워주는 코드
    #posts = Blog.objects.all()
    
    #날짜를 기준으로 정렬하여 가져오기
    posts = Blog.objects.filter().order_by('-date')
    return render(request,'index.html',{'posts':posts})

def new(request):
    return render(request,'new.html')

#블로그 글을 DB에 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()
        #html의 이름들과 대응
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save()
    return redirect('home')

#GET과 POST 요청을 한번에 처리 할 수 있는 함수
#GET -> 입력을 받을 수 있는 html
#POST -> 입력한 게시글을 서버로 전달
def djangonew(request):
    #GET 요청이 들어왔을 때
    if(request.method == 'GET'):
        form = BlogForm()
        return render(request,'django_new.html',{'form':form})

    #POST 요청이 들어왔을 때
    else:
        form = BlogForm(request.POST)
        if form.is_valid():
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.date = timezone.now()
            post.save()
            return redirect('home')
    
def modelnew(request):
    #GET 요청이 들어왔을 때
    if(request.method == 'GET'):
        form = BlogModelForm()
        return render(request,'django_new.html',{'form':form})

    #POST 또는 FILES 요청이 들어왔을 때
    else:
        form = BlogModelForm(request.POST,request.FILES)
        if form.is_valid():
            #모델 폼은 자체적으로 save 기능을 가지고 있다.
            form.save()
            return redirect('home')

def detail(request, id):
    #get_object_or_404 함수에 table과 pk값을 인자로 넘겨주어 한개의 column을 불러옴
    blog_detail = get_object_or_404(Blog,pk=id)
    comment_form = CommentForm()

    return render(request,'detail.html', {'post_info':blog_detail,'comment_form':comment_form})

def createcomment(request, post_id):
    mid_form = CommentForm(request.POST)
    if mid_form.is_valid():
        fin_form = mid_form.save(commit=False)
        fin_form.post = get_object_or_404(Blog,pk=post_id)
        fin_form.save()
        return redirect('detail',post_id)


# Create your views here.
