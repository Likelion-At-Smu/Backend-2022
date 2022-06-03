from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# 로그인해
def login(request):
    # request == POST 로그인 시키기
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)
        # username, password에 일치하는 회원이 있다면 그 회원에 해당하는 유저객체를 반환하고 없다면 none을 반환
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    # request == GET login.html 띄우기
    else:
        return render(request, 'login.html')

# 로그아웃해
def logout(request):
    auth.logout(request)
    return redirect('home')

# 회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password']) #새로운 유저객체를 만듦
            # 로그인해서 홈으로 리다이렉트 시켜줌
            auth.login(request, new_user)
            return redirect('home')
    # 예외처리 해줘야할듯??
    return render(request, 'register.html')