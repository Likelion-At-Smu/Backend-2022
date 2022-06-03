from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
def login(request):
    #request가 post라면 로그인 시키기
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, paswsword = password)

        #반환 받은 user가 none이 아니라면
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        #존재하는 회원이 아니라면
        else:
            return render(request, 'bad_login.html')
    #request가 get이라면 로그인 html띄우기
    else:
        return render(request, 'login.html')

def logout(request):
    # 로그아웃은 검증 할 게 없음
    auth.logout(request)
    # 로그아웃 후 home 화면으로 돌아가기
    return redirect('home')

def signup(request):
    # request 가 post라면
    if request.method == 'POST':
        # password 와 repeat가 같으면 회원가입을 시켜준다.
        if request.POST["password"]==request.POST["repeat"]:
            # 새로운 유저를 만들기
            new_user = User.objects.create_user(username = request.POST['Username'], password = request.POST['password'])
            new_user.save()
            # 로그인 하기
            auth.login(request, new_user,backend='django.contrib.auth.backends.ModelBackend')
            # 홈으로 돌아가기
            return redirect('home')
    return render(request, 'register.html')
    
