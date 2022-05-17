from django.shortcuts import render
import random

# Create your views here.
def lottoresult(request):
    num = int(request.GET['number'])
    lottolist = []
    for i in range(0,num):
        lottolist.append(random.sample(range(1,45),6))
    return render (request, 'lottoresult.html',{'result' : lottolist,'num' : num })