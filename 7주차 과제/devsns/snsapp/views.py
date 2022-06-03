from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost
from django.core.paginator import Paginator

def home(request):
    # posts = Post.objects.all()#모든 포스트 객체 가져오기
    posts = Post.objects.filter().order_by('-date')#데이트 오름차순으로 정렬한뒤에 가져오기
    Paginator(posts,5)#몇개단위로 무엇을 자를건가
    pagnum = request.GET.get('page')#몇번째 페이지 보는지 전송해야됨.
    posts = Paginator.get_page(pagnum)
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    if request.method == 'POST' or request.method == 'FILES': #request method가 POST일 경우
        form = PostForm(request.POST, request.FILES)#폼에 받은 값을 저장
        if form.is_valid():#유효하다면
            form.save()#입력값 저장
            return redirect('home')
    else:#GET일 경우
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})#딕셔너리 형태로 반환

def detail(request, post_id):#post_id값을 받는다
    post_detail = get_object_or_404(Post, pk=post_id)#pk값을 받는 get_object_or_404 메소드. 객체를 가져오고 만약 객체가 없다면 404를 띄워라
    comment_form = CommentForm()#코멘트 폼을 만들어서 리턴한다.
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form': comment_form})

# 댓글 저장
def new_comment(request, post_id):#뉴코멘트 함수
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)#아직은 완성되지않았으니까, 저장하지말고
        finished_form.post = get_object_or_404(Post, pk=post_id)#포스트 정보를 할당받음.
        finished_form.save()#그 뒤에 저장.
    return redirect('detail', post_id)


def freehome(request):#자유게시판 홈
    # posts = Post.objects.all()
    freeposts = FreePost.objects.filter().order_by('-date')#
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):#자유게시판 포스트 생성
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False) 
            unfinished.author = request.user            # user 추가!, 게시글에 누가 작성했는지 담아줘야한다.
            unfinished.save()#저장
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):#자유게시판 글 내용
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):#자유게시판 댓글
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
