from django.shortcuts import render, redirect
from django.contrib import auth # 로그인, 로그아웃기능, 이미 있는 회원인지 확인  
from django.contrib.auth.models import User 

def login(request) :
    # POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST' :
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd) # 이미 있는 회원인지
        if user is not None : 
            auth.login(request, user) # user객체로 로그인 
            return redirect('home')
        else: # None (존재하지 않는 회원) 
            return render(request, 'login.html')
    # GET 요청이 들어오면 login form을 담고 있는 login.html을 띄워줌 
    else :
        return render(request, 'login.html')

def logout(requset) :
    auth.logout(requset)
    return redirect('home')