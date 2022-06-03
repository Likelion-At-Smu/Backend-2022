from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost

# pagination 기능 사용하기 위해 import해야 할 것
from django.core.paginator import Paginator

def home(request):
    # post의 목록들을 query set의 형식으로 가져오기
    
    # 다 가져오기
    # posts = Post.objects.all()

    posts = Post.objects.filter().order_by('-date') # 내림차순
    # Paginator를 이용해 posts를 5개씩 나눠줄거야
    paginator = Paginator(posts, 5)
    # 몇 번째 페이지 갖고올거냐
    pagnum = request.GET.get('page')
    posts = paginator.get_page(pagnum)
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    # request method가 POST일 경우 입력값 저장
    if request.method == "POST" or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)
        
        # form에 입력된 값들이 유효하다면
        if form.is_valid():
            form.save()
            # 저장하고 home으로 redirect해라
            return redirect('home')
    # request method가 GET일 경우 form 입력 html 띄우기(else일 경우)
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    # 특정 객체 하나를 갖고오기(post_id에 맞는 객체)
    # 루트 : index.html의 post.id -> urls.py의 post_id -> views.py
    post_detail = get_object_or_404(Post, pk=post_id)
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form':comment_form})

def new_comment(request, post_id):
    # 댓글 저장해주는 기능 구현해주면 됨
    filed_form = CommentForm(request.POST)
    if filed_form.is_valid():
        finish_form = filed_form.save(commit=False)
        finish_form.post = get_object_or_404(Post, pk=post_id)
        finish_form.save()
    # 내가 댓글 단 게시글의 detail 페이지로 redirect
    return redirect('detail', post_id)

def freehome(request):
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        # 댓글처럼 author에 user 객체를 담아줘야 함(author는 user 참조한 것이므로)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.author = request.user # user 추가
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    # detail과 같음
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    # new_comment와 같음
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)