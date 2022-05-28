from django.shortcuts import render

# Create your views here.

# 요청이 들어왔을 때 index.html을 렌더링 해주는 함수
def home(request):
    return render(request, 'index.html')

def test(request):
    return render(request, 'test.html')