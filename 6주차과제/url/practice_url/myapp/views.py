from django.shortcuts import render

def first(requset) : 
    return render(requset, 'first.html') # 요청이 들어오면 -> first.html을 찍어준다

def second(request) :
    return render(request,'second.html')