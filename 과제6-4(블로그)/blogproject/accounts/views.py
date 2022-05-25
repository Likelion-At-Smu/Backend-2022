from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    #POST 요청이 들어오면 로그인 처리를 해주고
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')

        # //authenticate// -> 사용자가 입력한 아이디 패스워드가 실제로 데이터베이스에 있는지 검사해준다
        #이미 저장되어있는 회원이면 그 유저 객체를 반환하고 아니면 non을 반환
    #GET 요정이 들어오면 로그인 form을 담고 있는 login.html을 띄워주는 역할 
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')