from django.shortcuts import render, redirect, get_object_or_404 
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm

def home(request) :
    # 블로그 글들을 모조리 띄우는 코드
    # posts = Blog.objects.all()
    posts =Blog.objects.filter().order_by('-date') # 날짜를 기준으로 정렬, -는 내림차순 
    return render(request,'index.html',{'posts':posts})

# 블로그 글 작성 html을 보여주는 함수 
def new(request) :
    return render(request,'new.html')

# 블로그 글을 저장해주는 함수 
def creat(request) :
    if(request.method == 'POST') : # 들어온 요청이 POST요청이라면 
        post = Blog() # Blog 객체 생성
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.date = timezone.now()
        post.save() # 데이터베이스에 저장
    return redirect('home') # home 즉, index.html로 다시 돌아감 

# django form을 이용해서 입력값을 받는 함수 
# get요청(=입력값을 받을 수 있는 html을 가져다줌)과 
# post요청(=입력한 내용을 데이터베이스에 저장, form에서 입력한 내용을 처리)을 둘 다 처리가 가능한 함수 
def formcreat(request) :
    if request.method == 'POST' :
        # 입력 내용을 DB에 저장 
        form.BlogForm(request.POST) # 파일업로드까지 할 경우에는 requset.FILES도 추가해줘야함
        if form.is_valid() : # form에 입력한 값이 유효하다면 
            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save()
            return redirect('home')
    else : # get요청인 경우 
        # 입력을 받을 수 있는 html 가져다주기
        form = BlogForm()
    return render(request,'form_create.html',{'form':form}) # render()의 세번째 인자로 views.py 내의 데이터를 html에 넘겨줄 수 있음 
                                               # 단, 딕셔너리 자료형으로 넘겨줘야함 

def modelformcreat(request) :
    if request.method == 'POST' or request.method == 'FILES' :
        form = BlogModelForm(request.POST, request.FILES)
        if form.is_valid() :  
            form.save()
            return redirect('home')
    else : 
        form = BlogModelForm()
    return render(request,'form_create.html',{'form':form}) 

def detail(request, blog_id) :
    # blog_id 번째 블로그 글을 갖고와서 detail.html로 띄워주는 코드 
    # get_object_or_404는 pk값을 이용해 특정 모델 객체 하나만 가지고오기 위해 사용
    blog_detail = get_object_or_404(Blog, pk= blog_id)

    comment_form = CommentForm()

    return render(request,'detail.html',{'blog_detail':blog_detail, 'comment_form':comment_form})

def creat_comment(requset, blog_id) :
    filled_form = CommentForm(requset.POST)

    if filled_form.is_valid() :
        finshed_form = filled_form.save(commit=False) # 일단은 저장하지 않고 대기 
        finshed_form.post = get_object_or_404(Blog,pk=blog_id) 
        finshed_form.save()

    return redirect('detail', blog_id)                     