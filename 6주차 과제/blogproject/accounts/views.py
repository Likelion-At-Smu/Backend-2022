from django.shortcuts import render, redirect
#database 에 존재하는지 여부를 판단
from django.contrib import auth
#user객체를 사용
from django.contrib.auth.models import User
# Create your views here.

def login(request):
    #post : 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']

        #사용자가 입력한 request가 database 에 있는지 확인
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:#가입 되있는 경우
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'bad_login.html')

    #get : login form 띄워주기
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('home')