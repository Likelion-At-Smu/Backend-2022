from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost 
from django.core.paginator import Paginator # paginator가 객체들의 목록을 끊어서 보여준다
# query set의 형식으로 가지고 오고 싶으므로 models.py로 부터 Post를 가져온다


#-------_!  django에서는 이렇게 한가지 url에서--------------------------------
#--------! POST 요청과 GET요청을 둘다 처리할 수 있다-----------------
    # request method가 GET일 경우
        #form 입력 html 띄우기
def home(request):
    # posts = Post.objects.all() # Post의 객체들을 다 가져와라
    posts = Post.objects.filter().order_by('-date')
    paginator = Paginator(posts, 5) # posts를 몇개씩 끊어줄것인가 여기서는 5개씩
    pagenum = request.GET.get('page') 
    #객체들 중에서 몇번째를 가져올지 필요하기 때문에 request.GET요청을 보낼건데
    # page 몇번에 해당하는 숫자를 가져올거다라는 의미
    posts = paginator.get_page(pagenum) 
    #위에서 가져온 pagenum에 해당하는 숫자가 get_page에 담겨서 그만큼 짜른 개체가
    # posts에 담길 것이고 그 posts가 요청이 될것이다
    return render(request, 'index.html', {'posts':posts})

def postcreate(request):
    #request method가 POST일 경우
            #입력값 저장
    if request.method == "POST" or request.method == 'FILES':
        form = PostForm(request(request.POST, request.FILES))
        if form.is_valid():  # form에 담긴 값들이 유효하다면
            form.save()
            return redirect() #redirect 쓰려면 render옆에 import 해야한다
    # request method가 GET일 경우
    #form 입력 html 띄우
    else: 
        form = PostForm()
    return render(request, 'post_form.html', {'form':form})

def detail(request, post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    #post_id는 index.html에서 url 'detai' post_id에서 온것
    comment_form = CommentForm()
    return render(request, 'detail.html', {'post_detail':post_detail}, {'comment_form':comment_form})

def new_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)#채워야할 정보들
        finished_form.save()
    return redirect('detail', post_id)


def logout(request):
    auth.logout(request)
    return redirect('home')

def freehome(request):
    freeposts = FreePost.objects.filter().order_by('-date')
    return render(request, 'free_index.html', {'freeposts': freeposts})

def freepostcreate(request):
    if request.method == "POST" or request.method == 'FILES':
        form = FreePostForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished .author = request.user
            unfinished.save()
            return redirect('freehome')
    else:
        form = FreePostForm()
    return render(request, 'free_post_form.html', {'form':form})

def freedetail(request, post_id):
    post_detail = get_object_or_404(FreePost, pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'free_detail.html', {'post_detail':post_detail})

#자유 게시판에서 댓글 작성
def new_freecomment(request, post_id):
    filled_form = FreeCommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(FreePost, pk=post_id)#채워야할 정보들
        finished_form.save()
    return redirect('freedetail', post_id)

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')
