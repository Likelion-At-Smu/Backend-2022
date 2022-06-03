from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm, CommentForm, FreePostForm, FreeCommentForm
from .models import Post, FreePost
from django.core.paginator import Paginator

def home(request) :
    return render(request, "index.html")

def posttable(request) :
    posts = Post.objects.filter().order_by('-date')
    #한 페이지에 게시글이 10개만 보이도록 페이지네이트
    paginator = Paginator(posts, 3)
    #page를 dictionary 형태로 담아 page url로 설계한 것
    pagenum = request.GET.get('page')
    posts = paginator.get_page(pagenum)
    return render(request, "tables.html", {'posts':posts})

def postcreate(request) :
    if request.method == "POST" or request.method== "FILES":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posttable')
    else:
        form = PostForm()
    #form이라는 변수를 'form'이라는 key값에 value로 담아서 post_form.html에 정보를 전달
    return render(request, 'post_form.html', {'form':form})

def postdetail(request, post_id) :
    post_detail = get_object_or_404(Post,pk=post_id)
    comment_form = CommentForm()
    return render(request, 'postdetail.html', {'post_detail':post_detail,'comment_form':comment_form})

def commentcreate(request, post_id) :
    mid_form = CommentForm(request.POST)
    if mid_form.is_valid():
        fin_form = mid_form.save(commit='False')
        fin_form.post = get_object_or_404(Post, pk=post_id)
        fin_form.save()
    return redirect('postdetail', post_id)

def freeposttable(request) :
    posts = FreePost.objects.filter().order_by('-date')
    return render(request, "freetables.html", {'posts':posts})

def freepostcreate(request) :
    if request.method == "POST" or request.method== "FILES":
        mid_form = FreePostForm(request.POST, request.FILES)
        if mid_form.is_valid():
            fin_form = mid_form.save(commit=False)
            #최종 폼에 요청을 보낸 사용자 정보를 추가하여 저장
            fin_form.author = request.user
            fin_form.save()
            return redirect('freeposttable')
    else:
        form = FreePostForm()
    #form이라는 변수를 'form'이라는 key값에 value로 담아서 post_form.html에 정보를 전달
    return render(request, 'freepost_form.html', {'form':form})

def freepostdetail(request, post_id) :
    post_detail = get_object_or_404(FreePost,pk=post_id)
    comment_form = FreeCommentForm()
    return render(request, 'freepostdetail.html', {'post_detail':post_detail,'comment_form':comment_form})

def freecommentcreate(request, post_id) :
    mid_form = FreeCommentForm(request.POST)
    if mid_form.is_valid():
        fin_form = mid_form.save(commit=False)
        fin_form.post = get_object_or_404(FreePost, pk=post_id)
        fin_form.author = request.user
        fin_form.save()
    return redirect('freepostdetail', post_id)


# Create your views here.
