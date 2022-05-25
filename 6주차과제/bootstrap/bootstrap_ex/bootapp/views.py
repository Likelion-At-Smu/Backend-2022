from django.shortcuts import render

def home(requset) :
    return render(requset,'home.html')

def about(requset) :
    return render(requset,'about.html')
