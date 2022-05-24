from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    # post 요청 들어오면 로그인 처리 해줌
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    
    # get 요청 들어오면 login form 담고 있는 login.html 띄워줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
