from django.shortcuts import render, redirect
from django.contrib import auth #이것을 통해 로그인과 로그아웃 구현 가능
from django.contrib.auth.models import User

def login(request):#리퀘스트 타입이 POST라면 로그인 시키기
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)#이 메소드를 통해 로그인 구현 가능
        #authenticate는 유저정보가 있다면 유저정보를 반환하고, 없다면 none을 반환한다.
        if user is not None:#유저정보가 있다면
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):#회원가입하는 함수
    if request.method == "POST":#리퀘스트가 포스트였다면
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입하는 메소드
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')