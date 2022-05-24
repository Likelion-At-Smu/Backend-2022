from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

# portfolio-details.html 이동
def detail(request):
    return render(request, 'portfolio-details.html')
