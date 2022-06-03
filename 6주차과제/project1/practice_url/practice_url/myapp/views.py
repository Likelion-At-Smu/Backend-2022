from django.shortcuts import render

def first(request):
    return render(request, 'start.html')

def second(request):
    return render(request, 'second.html')
