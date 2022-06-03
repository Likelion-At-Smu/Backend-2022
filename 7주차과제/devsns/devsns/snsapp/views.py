from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost
from django.core.paginator import Paginator # 객체들의 목록을 끊어서 보여줌

def home(requset) :
    # posts = Post.objects.all() == 블로그 글들을 모조리 띄우는 코드
    posts = Post.objects.filter().order_by('-date')  # 날짜를 기준으로 정렬, -는 내림차순 
    paginator = Paginator(posts, 5) # 객체(posts)를 끊어서 나타냄, 몇 개씩 끊어서 보여줄 건지 뒤에 숫자로 나타냄 
    pagenum = requset.GET.get('page') # ?page=1 {page:1} 이 숫자(page에 매칭되는 수)를 받아오기위해서 사용
    posts = paginator.get_page(pagenum) 
    return render(requset,'index.html',{'posts':posts})

# 블로그 글을 저장해주는 함수 (modelform이용)
def postcreat(requset) :
    # requset가 POST인 경우 입력값 저장
    if requset.method == 'POST' or requset.method == 'FILES':
        form = PostForm(requset.POST, requset.FILES)
        if form.is_valid() :
            form.save()
            return redirect('home')
    # requset가 GET인 경우 form 입력 html 띄움
    else :
       form = PostForm() 
    return render(requset,'post_form.html',{'form':form})

def detail(requset, post_id) :
        # blog_id 번째 블로그 글을 갖고와서 detail.html로 띄워주는 코드 
        # get_object_or_404는 pk값을 이용해 특정 모델 객체 하나만 가지고오기 위해 사용
        post_detail = get_object_or_404(Post, pk= post_id) 
        comment_form = CommentForm()
        return render(requset,'detail.html',{'post_detail': post_detail,'comment_form':comment_form})

# 댓글 저장 
def new_comment(request, post_id) :
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid() :
        finshed_form = filled_form.save(commit=False) # 일단은 저장하지 않고 대기 
        finshed_form.post = get_object_or_404(Post,pk=post_id) # 여기에 담아준 다음
        finshed_form.save() # 저장 
    return redirect('detail', post_id)

def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False) # 아직 저장하지말고 
            # user 객체를 author에 추가
            unfinished.author = request.user         
            unfinished.save() # user를 추가한 뒤 저장 
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id) 
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
