from django.shortcuts import render

def productlist(requset) : 
    return render(requset, 'productlist.html') # 요청이 들어오면 -> first.html을 찍어준다

def productfirst(request) :
    return render(request,'productfirst.html')