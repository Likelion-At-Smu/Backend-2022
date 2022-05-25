from django.shortcuts import render

def board(requset) : 
    return render(requset, 'board.html') # 요청이 들어오면 -> first.html을 찍어준다

def boardfirst(request) :
    return render(request,'boardfirst.html')