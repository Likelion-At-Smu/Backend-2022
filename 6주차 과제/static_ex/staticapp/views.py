from django.shortcuts import render

# Create your views here.

# home.html을 연결하는 함수
def home(request):
    return render(request, "home.html")