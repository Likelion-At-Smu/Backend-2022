from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    if (request.method == "POST"):
        username = request.POST["username"]
        pasword = request.POST["password"]
        user = auth.authenticate(request, username=username, pasword=pasword)
        #authenticate는 만약 username과 username이 일치한다면 그에 반한는 
        # username을 반환하고 아니면 none을 반환한다

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')
        #request == GET
        # login html  띄우기 
def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
        #회원가입
        # djano의 유저 객체에 추가하는 상황
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
    #새로운 유저가 new_user에 담긴다
        #로그인 
        auth.login(request, new_user)
        return redirect('home')
    return render(request, 'register.html')