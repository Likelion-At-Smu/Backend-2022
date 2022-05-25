from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from django.utils import timezone
from .forms import BlogForm, BlogModelForm, CommentForm
#get_object_or_404는 객체를 하나 갖고 오고 객체가 없다면 404를 띄워라


def home(request):
    #블로그 글들을 모조리 띄우는 코드
    #order_by는 정렬해서 가져올 것 이다
    # posts = Blog.objects.filter().order_by('-date')
    #날짜를 기준으로 정렬된 blog들의 객체가 다 가져와져서
    # quryset에 담겨진다  ('date') 는 오름차순
    # ('-date')는 내림차순
    posts = Blog.objects.all()
    return render(request, 'index.html',{'posts':posts}) 


#블로그 글 작성 html을 보여주는 함수
def new(request):
    return render(request, 'new.html') 

#블로그 글을 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        post = Blog()           # Blog 객체를 생성해서
        post.title = request.POST['title'] 
        post.body = request.POST['body']
        post.date = timezone.now()     
        post.save() #데이터베이스에 저장
    return redirect('home')
    # 함수가 정상적으로 끝났으면 home으로 다시 돌아간다(redirect)

#django form을 이용해서 입력값을 받는 함수
#GET 요청과 (=입력값을 받을 수 있는 html을 갖다 줘야함)
#POST 요청 (= 입력한 내용을 데이터베이스에 저장. form에서 입력한 내용을 처리)
#둘 다 처리가 가능한 함수

def formcreate(request):
        #입력을 받을 수 있는 html을 갖다주기
    if request.method == 'POST':        
        form = BlogForm(request.POST) # request에 POST를 담고 있는 from을 만들어준다
        if form.is_valid():  #입력값의 유효성을 검사하기 위해 사용한다

    #====아랫줄의 post는 model을 기반으로 만들어진 객체를 save 했다=== 그런데 modelform의 경우

            post = Blog()
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.save() #데이터 베이스에 저장
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'form_create.html', {'form':form})
    #render은 세번째 인자를 받을 수 있다
    #render()의 세번째 인자로 views.py내의 데이터를 html에 넘겨줄 수 있다.
    #단 딕셔너리 자료형으로 넘겨주어야 한다

def modelformcreate(request):

     #!======아래줄의 modelform으로 만든 form은 자체적으로 save method를 가지고 있다 
    #  그래서 form.save()하면 저장이 된다

    if request.method == 'POST' or request.method == 'FILES':
        form = BlogModelForm(request.POST, request.FILES) # request에 POST를 담고 있는 from을 만들어준다
        if form.is_valid():  #입력값의 유효성을 검사하기 위해 사용한다
            form.save()
            return redirect('home')
    else:
        form = BlogModelForm()
    return render(request, 'form_create.html', {'form':form})

    #@================= 중요 ==============@
    #render을 통해서 특정 html에 views.py의 데이터를 넘겨주고 싶으면
    # 세번째 인자로 딕셔너리 자료형으로 넘겨줄 수 있다.
    # 그리고 넘겨준 대상은 중괄호 2개로써 {{   ???  }}  html 안에다가 찍어 줄 수 있다

def detail(request, blog_id):
    #blog_id 번쨰 블로그 글을 갖고 와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    #블로그 객체를 하나 갖고 어떤 객체냐면 pk값이 블로그 id인 id값을 가져올거다.
    #blog_id번째 블로그 글을  detail.html로 띄워주는 코드
    return render(request, 'detail.html', {'blog_detail':blog_detail} )

    comment_form = CommentForm()

    return render(request, 'detail.html', {'blog_detail':blog_detail}, {'comment_form':comment_form})

def create_comment(request, blog_id):
    filled_form = CommentForm(request.POST)
    # filled form은 comment를 기준으로 만들어짐

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        #아직 저장중이지 않고 대기중인 form을 finished_form에 담아준다
        finished_form.post = get_object_or_404(Blog, pk=blog_id)
        #블로그 개체중 pk값이 blog_id인것을 담아준다
        finished_form.save()
        #그리고 저장한다

    return redirect('detail', blog_id)