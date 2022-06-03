from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreeCommentForm, FreePostForm
from .models import Post, FreePost
# 객체들의 목록들을 끊어서 보여주기위해서
from django.core.paginator import Paginator

def home(request):
    # filter를 이용해서 models.py에서 날짜의 오름차순으로 post의 객체들을 가져와라
    posts = Post.objects.filter().order_by('-date')
    # 객체들의 목록들을 숫자만큼 끊어준다
    paginator = Paginator(posts,5)
    # page number에 대한 정보를 get요청
    pagnum = request.GET.get('page')
    # get요청을 통해 가져온 페이지 넘버에 해당하는 객체가 posts에 저장된다.
    posts = paginator.get_page(pagnum)
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    #request가 post일경우 이고 request.method가 file type일 경우
    if request.method == 'POST' or request.method == 'FILES':
        # form 에 request와 file을 담는다.
        form = PostForm(request.POST, request.FILES)
        # 유효한 값들이 담겨있다면
        if form.is_valid():
            # 저장하기
            form.save()
            # 저장이 완료되면 home으로 돌아가기
            return redirect('home')
    # request가 get일 경우
    else:
        # form을 입력할 수 있는 form을 보내준다.
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

# post 객체로 부터 post_id라는 두번째 인자를 받는다.
def detail(request, post_id):
    # pk값이 post_id에 해당하는 post_detail 이 변수안에 담기고 실패하면 404 실행
    post_detail = get_object_or_404(Post, pk=post_id)
    #글 상세 페이지에 댓글이 보이게 한다.
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail, 'comment_form': comment_form})

# 댓글 저장
def new_comment(request, post_id):
    # post요청을 보낸 form을 저장한다.
    filled_form = CommentForm(request.POST)
    # data 가 유효하다면
    if filled_form.is_valid():
        # 아직 저장하지 말고 
        finished_form = filled_form.save(commit=False)
        # 특정 게시물의 정보를 담아준다
        finished_form.post = get_object_or_404(Post, pk=post_id)
        # 저장한다.
        finished_form.save()
    return redirect('detail', post_id)


def freehome(request):
    # 자유게시판 객체들을 목록으로 날짜의 오름차순으로 띄워라
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})


def freepostcreate(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            # 글을 작성한 유저 객체를 담는다.
            unfinished.author = request.user            # user 추가!
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})


def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    # 자유게시판 댓글
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail, 'comment_form': comment_form})


def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)
        finished_form.save()
    return redirect('freedetail', post_id)
