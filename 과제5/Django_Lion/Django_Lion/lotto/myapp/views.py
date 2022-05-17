from django.shortcuts import render
import random
def home(request):
    return render(request, 'index.html')

def result(request):
    num = int(request.GET.get('number')) 
    list = []
    for i in range(0, num):
        list.append(random.sample(range(1,45),6))
    return render(request, 'result.html', {'result' : list, 'num' : num })
# Create your views here.
